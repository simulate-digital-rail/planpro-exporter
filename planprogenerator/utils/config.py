from dataclasses import dataclass
from typing import Literal

@dataclass
class Config:
    author_name: str
    coord_representation:  Literal['wgs84', 'dbref']
    organisation: str
