from typing import List

from cwapi3d_fake.cwapi3d_api import utils
from cwapi3d_fake.cwapi3d_api.utils import Material

data = utils.load_data()


def create_material(name: str) -> int:
    """Creates new material

    Parameters:
        name: name

    Returns:
        material ID
    """
    existing_materials: List[Material] = utils.retrieve_materials_from_data(data['materials'])

    material_names = [attr.material_name for attr in existing_materials]
    if any(material_name == name for material_name in material_names):
        return [attr.material_id for attr in existing_materials if attr.material_name == name][0]
    material_id = utils.create_random_6_digit_number()
    new_material = {
        str(material_id):
            name
    }
    data['materials'].update(new_material)
    utils.persist_data(data)

    return material_id


def set_name(material_id: int, name: str) -> None:
    """Sets the material name

    Parameters:
        material_id: material_id
        name: name

    Returns:
        None
    """
    existing_materials: List[Material] = utils.retrieve_materials_from_data(data['materials'])
    result = list(filter(lambda item: int(item.material_id) == material_id, existing_materials))
    if len(result) > 0:
        data['materials'][str(material_id)]['name'] = name
        utils.persist_data(data)


def set_code(material_id: int, code: str) -> None:
    existing_materials: List[Material] = utils.retrieve_materials_from_data(data['materials'])
    result = list(filter(lambda item: int(item.material_id) == material_id, existing_materials))
    if len(result) > 0:
        data['materials'][str(material_id)]['code'] = code
        utils.persist_data(data)


def get_material_id(material_name: str) -> int:
    """Gets the material with a given name

    Parameters:
        material_name: material_name

    Returns:
        material ID
    """
    existing_materials: List[Material] = utils.retrieve_materials_from_data(data['materials'])
    result = list(filter(lambda item: item.material_name == material_name, existing_materials))
    if len(result) > 0:
        return result[0].material_id
    return 0


def get_name(material_id: int) -> str:
    """Gets the material name

    Parameters:
        material_id: material_id

    Returns:
        material name
    """
    existing_materials: List[Material] = utils.retrieve_materials_from_data(data['materials'])
    result = list(filter(lambda item: item.material_id == material_id, existing_materials))
    if len(result) > 0:
        return result[0].material_name
    return ''


def get_code(material_id: int) -> str:
    existing_materials: List[Material] = utils.retrieve_materials_from_data(data['materials'])
    result = list(filter(lambda item: item.material_id == material_id, existing_materials))
    if len(result) > 0:
        return result[0].material_code
    return ''
