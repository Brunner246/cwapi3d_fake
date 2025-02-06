import os

if (fake_data := os.getenv('CWAPI3D_FAKE_Test')) == 'false' or fake_data is None:
    os.environ['CWAPI3D_FAKE_Test'] = 'true'

from cwapi3d_fake.cwapi3d_api.material_controller import create_material, get_material_id, get_name, set_name, get_code, \
    set_code


def test_create_material():
    new_material_name = 'C24'
    create_material(new_material_name)

    material_id = get_material_id(new_material_name)
    material_name = get_name(material_id)

    assert material_name == new_material_name

def test_set_name():
    set_name(654330, 'CLT-B')
    assert get_name(654330) == 'CLT-B'

def test_get_code():
    set_code(654330, "0x20")
    assert get_code(654330) == "0x20"

