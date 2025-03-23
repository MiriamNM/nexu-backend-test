from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import create_brand, create_model, get_models, get_brands
from app.database import get_db

from app.schemas import BrandCreate, BrandResponse, ModelCreate, Model

router = APIRouter()


@router.get("/", response_model=str)
async def hello_world():
    return "Hola Mundo"


@router.get("/brands", response_model=list[BrandResponse])
async def list_brands(db: AsyncSession = Depends(get_db)):
    return await get_brands(db)


@router.post("/brands", response_model=BrandResponse)
async def add_brand(brand: BrandCreate, db: AsyncSession = Depends(get_db)):
    return await create_brand(db, brand)


@router.get("/brands/{id}/models", response_model=list[Model])
async def list_models(id: int, db: AsyncSession = Depends(get_db)):
    return await get_models(db, id)


@router.post("/brands/{id}/models", response_model=Model)
async def add_model(id: int, model: ModelCreate, db: AsyncSession = Depends(get_db)):
    return await create_model(db, id, model)
