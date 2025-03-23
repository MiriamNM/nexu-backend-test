from pydantic import BaseModel
from typing import List, Optional


class ModelBase(BaseModel):
    name: str
    average_price: Optional[float] = None


class ModelCreate(ModelBase):
    pass


class Model(ModelBase):
    id: int

    class Config:
        orm_mode = True


class BrandBase(BaseModel):
    name: str


class BrandCreate(BrandBase):
    pass


class BrandResponse(BrandBase):
    id: int
    average_price: float
    models: List[Model] = []

    class Config:
        orm_mode = True
