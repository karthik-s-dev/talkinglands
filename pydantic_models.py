from pydantic import BaseModel, Field

class PointModel(BaseModel):
    name: str
    description: str = None
    location: list[float]