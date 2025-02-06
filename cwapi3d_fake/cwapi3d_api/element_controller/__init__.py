from typing import List

from cwapi3d_fake.cwapi3d_api import utils
from cwapi3d_fake.cwapi3d_api.cadwork.point_3d import point_3d

data = utils.load_data()


def create_rectangular_beam_points(width: float, height: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create rectangular beam points

    Parameters:
        width: width
        height: height
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """

    new_element = utils.create_new_construction_element(width, height, p1, p2, p3)
    element_id = new_element['element_id']
    data['elements'].append(new_element)
    utils.persist_data(data)

    return element_id


def create_rectangular_panel_points(width: float, thickness: float, p1: point_3d, p2: point_3d, p3: point_3d) -> int:
    """create rectangular panel points

    Parameters:
        width: width
        thickness: thickness
        p1: p1
        p2: p2
        p3: p3

    Returns:
        int
    """
    new_element = utils.create_new_construction_element(width, thickness, p1, p2, p3)
    element_id = new_element['element_id']
    data['elements'].append(new_element)
    utils.persist_data(data)

    return element_id


def create_drilling_points(diameter: float, p1: point_3d, p2: point_3d) -> int:
    """create drilling points

    Parameters:
        diameter: diameter
        p1: p1
        p2: p2

    Returns:
        int
    """
    new_element = utils.create_new_connector_element(diameter, p1, p2)
    element_id = new_element['element_id']
    data['elements'].append(new_element)
    utils.persist_data(data)

    return element_id


def get_element_from_cadwork_guid(cadwork_guid: str) -> int:
    """get element from cadwork guid

    Parameters:
        cadwork_guid: cadwork_guid

    Returns:
        int
    """
    elements = list(filter(lambda element: element['cadwork_guid'] == cadwork_guid, data['elements']))
    if not elements:
        raise ValueError(f"Element with cadwork_guid {cadwork_guid} not found")
    return elements[0]['element_id']


def get_all_identifiable_element_ids() -> List[int]:
    """get all identifiable element ids

    Returns:
        List[int]
    """
    return [element['element_id'] for element in data['elements']]


def get_active_identifiable_element_ids() -> List[int]:
    """get active identifiable element ids

    Returns:
        List[int]
    """
    return [element['element_id'] for element in data['elements'][::3]]


def get_element_cadwork_guid(element_id: int) -> str:
    """get element cadwork guid

    Parameters:
        element_id: element_id

    Returns:
        str
    """
    result = list(filter(lambda element: element['element_id'] == element_id, data['elements']))
    if len(result) > 0:
        return result[0]['cadwork_guid']
    raise ValueError(f"Element with element_id {element_id} not found")
