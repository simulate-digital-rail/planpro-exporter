from typing import Literal
import pyproj

from planprogenerator.model.node import Node

def convert_coords(x, y, coord_representation: Literal['wgs84', 'dbref']):
    if coord_representation == 'wgs84':
        proj_wgs84 = pyproj.Proj(init="epsg:4326")
        proj_gk4 = pyproj.Proj(init="epsg:31468")
        x_new, y_new = pyproj.transform(proj_wgs84, proj_gk4, y, x)
        return x_new, y_new
    else:
        return x, y
