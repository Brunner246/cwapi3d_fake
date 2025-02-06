import os

if (fake_data := os.getenv('CWAPI3D_FAKE_Test')) == 'false' or fake_data is None:
    os.environ['CWAPI3D_FAKE_Test'] = 'true'

from cwapi3d_fake.cwapi3d_api.attribute_controller import set_name, set_subgroup, get_subgroup, set_user_attribute_name, \
    get_user_attribute, set_element_material, get_element_material_name, get_user_attribute_name, is_beam

import json


def test_set_name():
    set_name([1848469355, 1848469387], 'new name')
    with open('data.json', 'r') as file:
        data = json.load(file)
    elements = list(filter(lambda element: element['element_id'] in [1848469355, 1848469387], data['elements']))
    assert all(element['name'] == 'new name' for element in elements)


def test_set_subgroup():
    subgroup_1: str = get_subgroup(1848469355)
    subgroup_2: str = get_subgroup(1848469387)
    set_subgroup([1848469355, 1848469387], 'new subgroup')
    with open('data.json', 'r') as file:
        data = json.load(file)
    elements = list(filter(lambda element: element['element_id'] in [1848469355, 1848469387], data['elements']))
    assert len(elements) == 2
    assert all(element['subgroup'] == 'new subgroup' for element in elements)

    do_reset_subgroup_values(elements, [subgroup_1, subgroup_2])


def do_reset_subgroup_values(elements, subgroup_values):
    [set_subgroup([element['element_id']], subgroup)
     for element, subgroup in zip(elements, subgroup_values)]


def test_set_user_attribute_name():
    set_user_attribute_name(15, 'Hackathon 2025')
    user_attribute = get_user_attribute(1848469355, 15)
    assert user_attribute == 'Hackathon 2025'


def test_set_element_material():
    set_element_material([1848469355], 654322)
    material_name = get_element_material_name(1848469355)
    assert material_name.lower() == 'Baubuche'.lower()


def test_get_user_attribute_name():
    user_attribute = get_user_attribute_name(1)
    assert user_attribute.lower() == 'user1'.lower()


def test_is_beam():
    assert is_beam(1848469417) == True
