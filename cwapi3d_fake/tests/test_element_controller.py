import math
import os
import pytest

if (fake_data := os.getenv('CWAPI3D_FAKE_Test')) == 'false' or fake_data is None:
    os.environ['CWAPI3D_FAKE_Test'] = 'true'

from unittest.mock import patch, mock_open
import json

from cwapi3d_fake.cwapi3d_api.cadwork.point_3d import point_3d
from cwapi3d_fake.cwapi3d_api.element_controller import get_element_from_cadwork_guid, create_rectangular_beam_points, \
    get_element_cadwork_guid
from cwapi3d_fake.tests.mock_data import mock_data


def test_get_element_from_cadwork_guid():
    valid_guid = "{E7CEAE8D-871B-4EF8-8EBB-49B36EA87552}"
    assert get_element_from_cadwork_guid(valid_guid) == 1848469387

    valid_guid = "{A1B2C3D4-E5F6-7890-1234-56789ABCDEF0}"
    assert get_element_from_cadwork_guid(valid_guid) == 1848689940

    invalid_guid = "{INVALID-GUID-1234-5678-9ABC-DEF012345678}"
    with pytest.raises(ValueError, match=f"Element with cadwork_guid {invalid_guid} not found"):
        get_element_from_cadwork_guid(invalid_guid)


@patch('builtins.open', new_callable=mock_open, read_data=json.dumps(mock_data))
@patch('json.dump')
def test_create_rectangular_beam_points(mock_json_dump, mock_file):
    width = 180.0
    height = 60.0
    p1 = point_3d(3090.0, 1250.0, 3070.0)
    p2 = point_3d(3090.0, 1250.0, 5550.0)
    p3 = point_3d(3090.0, 1251.0, 3070.0)

    new_id: int = create_rectangular_beam_points(width, height, p1, p2, p3)
    assert new_id != 0

    data = json.loads(mock_file().read())
    data['elements'][-1]['element_id'] = new_id

    assert any(element['element_id'] == new_id for element in data['elements'])
    assert any(math.isclose(element['geometry']['width'], width) for element in data['elements'])


def test_get_element_cadwork_guid():
    guid = get_element_cadwork_guid(1848689945)
    assert guid == "{F4G5H6I7-J8K9-0123-4567-89ABCDEF005}"
