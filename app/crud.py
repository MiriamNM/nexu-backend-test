from sqlalchemy.orm import Session
from . import models, schemas

# CRUD para Brand


def get_brands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brand).offset(skip).limit(limit).all()


def get_brand(db: Session, brand_id: int):
    return db.query(models.Brand).filter(models.Brand.id == brand_id).first()


def create_brand(db: Session, brand: schemas.BrandCreate):
    db_brand = models.Brand(name=brand.name)
    db.add(db_brand)
    db.commit()
    db.refresh(db_brand)
    return db_brand

# CRUD para Model


def get_models(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Model).offset(skip).limit(limit).all()


def create_model(db: Session, model: schemas.ModelCreate, brand_id: int):
    db_model = models.Model(**model.dict(), brand_id=brand_id)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model
