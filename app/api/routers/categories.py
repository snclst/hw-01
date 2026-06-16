from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_category_service
from app.schemas.cats_scem import CategorySchema, CategoryCreateSchema
from app.services.categories import CatsNotFoundError, CategoryService


routers = APIRouter(prefix='/categories', tags=['categories'])


@routers.get("", response_model=list[CategorySchema])
def get_categories(service: CategoryService = Depends(get_category_service)) -> list[CategorySchema]:
    return service.list_category()

@routers.post("", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
def create_category(
    payload: CategoryCreateSchema,
    service: CategoryService = Depends(get_category_service),
) -> CategorySchema:
    return service.create_category(payload)

@routers.patch("/{category_id}", response_model=CategorySchema)
def update_category(
    category_id: str,
    payload: CategorySchema,
    service: CategoryService = Depends(get_category_service),
) -> CategorySchema:
    try:
        return service.update_category(category_id, payload)
    except CategoryNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена",
        )


@routers.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: str,
    service: CategorySchema = Depends(get_category_service),
) -> None:
    try:
        service.delete_category(category_id)
    except CatsNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Категория не найдена",
        )