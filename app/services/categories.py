from sqlalchemy.orm import Session

from app.repositories.categories import CategoryRepository
from app.schemas.cats_scem import  CategorySchema, CategoryCreateSchema, CategoryUpdateSchema


class CatsNotFoundError(Exception):
    pass


class CategoryService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = CategoryRepository(db)

    def list_category(self) -> list[CategorySchema]:
        categories = self.repository.get_all_cat()
        return [CategorySchema.model_validate(category) for category in categories]

    def create_category(self, payload: CategoryCreateSchema) -> CategorySchema:
        category = self.repository.create_cat(title=payload.name)
        self.db.commit()
        return CategorySchema.model_validate(category)

    def update_category(self, category_id: str, payload: CategoryUpdateSchema) -> CategorySchema:
        category = self.repository.get_by_id_cat(category_id)

        if payload.name is not None:
            category.title = payload.name

        self.db.commit()
        return CategorySchema.model_validate(category)

    def delete_category(self, category_id: str) -> None:
        category = self.repository.get_by_id_cat(category_id)

        self.repository.delete(category)
        self.db.commit()