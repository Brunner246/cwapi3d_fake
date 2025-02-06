from typing import List
from cwapi3d_fake.cwapi3d_api import utils
from cwapi3d_fake.cwapi3d_api.cadwork.point_3d import point_3d

data = utils.load_data()


def get_width(element_id: int) -> float:
    """get width

    Parameters:
        element_id: element_id

    Returns:
        float
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['geometry']['width']
    return 0.0


def get_height(element_id: int) -> float:
    """get height

    Parameters:
        element_id: element_id

    Returns:
        float
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['geometry']['height']
    return 0.0


def get_length(element_id: int) -> float:
    """get length

    Parameters:
        element_id: element_id

    Returns:
        float
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['geometry']['length']
    return 0.0


def get_p1(element_id: int) -> point_3d:
    """get p1

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        p1 = element['geometry']['p1']
        return point_3d(p1[0], p1[1], p1[2])
    return point_3d(0.0, 0.0, 0.0)


def get_p2(element_id: int) -> point_3d:
    """get p2

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        p2 = element['geometry']['p2']
        return point_3d(p2[0], p2[1], p2[2])
    return point_3d(0.0, 0.0, 0.0)


def get_p3(element_id: int) -> point_3d:
    """get p3

    Parameters:
        element_id: element_id

    Returns:
        point_3d
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        p3 = element['geometry']['p3']
        return point_3d(p3[0], p3[1], p3[2])
    return point_3d(0.0, 0.0, 0.0)
