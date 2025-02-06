from typing import List
from cwapi3d_fake.cwapi3d_api import utils

data = utils.load_data()


def set_name(element_id_list: List[int], name: str) -> None:
    """Sets the element name

    Parameters:
        element_id_list: element_id_list
        name: name

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(map(lambda element: element.update({'name': name}), elements))
    utils.persist_data(data)


def set_group(element_id_list: List[int], group: str) -> None:
    """Sets the element group

    Parameters:
        element_id_list: element_id_list
        group: group

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(map(lambda element: element.update({'group': group}), elements))
    utils.persist_data(data)


def set_subgroup(element_id_list: List[int], subgroup: str) -> None:
    """Sets the element subgroup

    Parameters:
        element_id_list: element_id_list
        subgroup: subgroup

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(map(lambda element: element.update({'subgroup': subgroup}), elements))
    utils.persist_data(data)


def set_user_attribute(element_id_list: List[int], number: int, user_attribute: str) -> None:
    """Sets the element user attribute

    Parameters:
        element_id_list: element_id_list
        number: number
        user_attribute: user_attribute

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(map(lambda element: element['user_attributes'].update({str(number): user_attribute}), elements))
    utils.persist_data(data)


def set_production_number(element_id_list: List[int], production_number: int) -> None:
    """Sets the element production number

    Parameters:
        element_id_list: element_id_list
        production_number: production_number

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(map(lambda element: element.update({'production_number': production_number}), elements))
    utils.persist_data(data)


def set_part_number(element_id_list: List[int], part_number: int) -> None:
    """Sets the element part number

    Parameters:
        element_id_list: element_id_list
        part_number: part_number

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(map(lambda element: element.update({'part_number': part_number}), elements))
    utils.persist_data(data)


def set_user_attribute_name(number: int, user_attribute_name: str) -> None:
    """Sets the user attribute name

    Parameters:
        number: number
        user_attribute_name: user_attribute_name

    Returns:
        None
    """
    [element['user_attributes'].update({str(number): user_attribute_name}) for element in data['elements']]
    utils.persist_data(data)


def set_element_material(element_id_list: List[int], material_id: int) -> None:
    """Sets the element material

    Parameters:
        element_id_list: element_id_list
        material_id: material

    Returns:
        None
    """
    elements = utils.get_elements_filter_by_ids(element_id_list, data)
    list(filter(lambda material: material['material'].update({'material_id': material_id}),
                elements))
    utils.persist_data(data)


def get_name(element_id: int) -> str:
    """Gets the element name

    Parameters:
        element_id: element_id

    Returns:
        element name
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['name']
    return ''


def get_group(element_id: int) -> str:
    """Gets the element group

    Parameters:
        element_id: element_id

    Returns:
        element group
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['group']
    return ''


def get_subgroup(element_id: int) -> str:
    """Gets the element subgroup

    Parameters:
        element_id: element_id

    Returns:
        element subgroup
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['subgroup']
    return ''


def get_comment(element_id: int) -> str:
    """Gets the element comment

    Parameters:
        element_id: element_id

    Returns:
        element comment
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['comment']
    return ''


def get_user_attribute(element_id: int, number: int) -> str:
    """Gets the element user attribute

    Parameters:
        element_id: element_id
        number: number

    Returns:
        element user attribute
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['user_attributes'].get(str(number), '')
    return ''


def get_production_number(element_id: int) -> int:
    """Gets the element production number

    Parameters:
        element_id: element_id

    Returns:
        element production number
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['production_number']
    return 0


def get_user_attribute_name(number: int) -> str:
    """Gets the user attribute name

    Parameters:
        number: number

    Returns:
        user attribute name
    """
    keys = data['elements'][0]['user_attributes'].get(str(number), '')
    if keys:
        return list(keys.keys())[0]
    return ''


def get_element_material_name(element_id: int) -> str:
    """Gets the element material name

    Parameters:
        element_id: element_id

    Returns:
        element material name
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        material_id = element['material'].get("material_id", 0)
        return data['materials'].get(str(material_id), '').get('name', '')
    return ''


def is_beam(element_id: int) -> bool:
    """Tests if element is beam

    Parameters:
        element_id: element_id

    Returns:
        is element beam
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['element_type'] == 'beam'
    return False


def is_panel(element_id: int) -> bool:
    """Tests if element is panel

    Parameters:
        element_id: element_id

    Returns:
        is element panel
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['element_type'] == 'plate'
    return False


def is_drilling(element_id: int) -> bool:
    """Tests if element is drilling

    Parameters:
        element_id: element_id

    Returns:
        is element drilling
    """
    element = utils.get_element_filter_by_id(element_id, data)
    if element:
        return element['element_type'] == 'drilling'
    return False
