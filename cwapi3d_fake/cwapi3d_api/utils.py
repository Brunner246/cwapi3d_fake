import json
import random
import uuid
import os
from typing import List, Any, Dict

from cwapi3d_fake.cwapi3d_api.cadwork.point_3d import point_3d

if os.getenv('CWAPI3D_FAKE_Test') == 'true':
    cwapi3d_fake_data_path = '../tests/data.json'
else:
    cwapi3d_fake_data_path = '../data/data.json'


def load_data():
    with open(cwapi3d_fake_data_path, 'r') as file:
        return json.load(file)


def save_data(data):
    with open(cwapi3d_fake_data_path, 'w') as file:
        json.dump(data, file, indent=4)


def create_random_10_digit_number() -> int:
    """create random 10 digit number

    Returns:
        int
    """
    return random.randint(1000000000, 9999999999)


def create_guid() -> str:
    """create guid

    Returns:
        str
    """
    return str(uuid.uuid4())


def create_fake_cadwork_element_template():
    element_id = create_random_10_digit_number()
    new_element = {
        "name": "",
        "user_attributes": {
        },
        "cadwork_guid": f"{{{create_guid()}}}",
        "element_type": "beam",
        "subgroup": "",
        "group": "",
        "material_name": "",
        "material_id": 0,
        "element_id": element_id
    }
    return new_element


def create_new_construction_element(width: float, height: float, p1: point_3d, p2: point_3d, p3: point_3d):
    new_element = create_fake_cadwork_element_template()
    new_element['geometry'] = {
        "width": width,
        "height": height,
        "p1": [p1.x, p1.y, p1.z],
        "p2": [p2.x, p2.y, p2.z],
        "p3": [p3.x, p3.y, p3.z]
    }
    return new_element


def create_new_connector_element(diameter: float, p1: point_3d, p2: point_3d):
    new_element = create_fake_cadwork_element_template()
    new_element['geometry'] = {
        "diameter": diameter,
        "p1": [p1.x, p1.y, p1.z],
        "p2": [p2.x, p2.y, p2.z]
    }
    return new_element


def get_elements_filter_by_ids(element_id_list: List[int], mock_data: Any) -> List[Dict]:
    return list(filter(lambda element: element['element_id'] in element_id_list, mock_data['elements']))


def get_element_filter_by_id(element_id: int, mock_data: Any) -> Dict[str, Any]:
    if (result := list(filter(lambda element: element['element_id']
                                              == element_id, mock_data['elements']))) is not None:
        return result[0]
    return {}
