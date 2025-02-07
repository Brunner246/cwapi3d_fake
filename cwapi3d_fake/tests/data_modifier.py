import json
import os
import random
import uuid

os.environ['CWAPI3D_FAKE_Test'] = 'true'

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
    for key, value in data['materials'].items():
        materials[key] = {'name': value,
                          'code': random.randint(100, 999)}
    data['materials'] = materials


def generate_unique_id():
    """Generate a short unique ID for reference values."""
    return random.randint(10_000, 99_999)


if __name__ == '__main__':
    with open(cwapi3d_fake_data_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # update_material_info()

    with open(cwapi3d_fake_data_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
