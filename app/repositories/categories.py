
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.categories import CategoryORM


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_cat(self) -> list[CategoryORM]:
        return self.db.scalars(select(CategoryORM)).all()

    def get_by_id_cat(self, category_id: str) -> CategoryORM | None:
        return self.db.get(CategoryORM, category_id)

    def create_cat(self, title: str) -> CategoryORM:
        category = CategoryORM(title=title)
        self.db.add(category)
        return category

    def delete(self, category: CategoryORM) -> None:
        self.db.delete(category)
