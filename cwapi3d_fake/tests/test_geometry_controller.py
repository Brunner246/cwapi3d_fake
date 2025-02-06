import math
import os

if (fake_data := os.getenv('CWAPI3D_FAKE_Test')) == 'false' or fake_data is None:
    os.environ['CWAPI3D_FAKE_Test'] = 'true'

from cwapi3d_fake.cwapi3d_api.geometry_controller import get_p2, get_length
from cwapi3d_fake.cwapi3d_api.cadwork.point_3d import point_3d


def test_get_p2():
    axis_point2 = get_p2(1848469355)
    assert axis_point2 == point_3d(3100.0, 1260.0, 5560.0)


def test_get_length():
    length = get_length(1848469355)
    assert math.isclose(length, 2480.0)
