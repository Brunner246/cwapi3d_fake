import json
import os
import random

os.environ['CWAPI3D_FAKE_Test'] = 'false'

if os.getenv('CWAPI3D_FAKE_Test') == 'true':
    cwapi3d_fake_data_path = 'data.json'
else:
    cwapi3d_fake_data_path = '../data/data.json'


def append_production_number_to_element():
    [element.update({'production_number': random.randint(1, 100)}) for element in data['elements']]


def append_part_number_to_element():
    [element.update({'part_number': random.randint(1, 100)}) for element in data['elements']]


def append_comment_to_element():
    [element.update({'comment': ""}) for element in data['elements']]


def update_material_info():
    materials = {}
    for element in data['elements']:
        material_id = element['material']['material_id']
        material_name = element['material'].pop('material_name')
        materials[material_id] = material_name

    data['materials'] = materials


def update_user_attributes():
    for element in data['elements']:
        updated_user_attributes = {}
        for key, value in element['user_attributes'].items():
            updated_user_attributes[key] = {f'user{key}': value}
        element['user_attributes'] = updated_user_attributes


if __name__ == '__main__':
    with open(cwapi3d_fake_data_path, 'r') as file:
        data = json.load(file)

    update_user_attributes()

    with open(cwapi3d_fake_data_path, 'w') as file:
        json.dump(data, file, indent=4)
