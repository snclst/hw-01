from pydantic import BaseModel, ConfigDict


class CategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str

class CategoryCreateSchema(BaseModel):
    name: str

class CategoryUpdateSchema(BaseModel):
    name: str
