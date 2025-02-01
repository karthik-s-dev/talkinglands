from pydantic import BaseModel, Field
from typing import List

class PointModel(BaseModel):
    name: str
    description: str = None
    location: list[float]

class PolygonModel(BaseModel):
    name: str
    description: str
    coordinates: List[List[List[float]]]