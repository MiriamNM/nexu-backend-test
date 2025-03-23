import json
from sqlalchemy.orm import Session
from app import models, database


def load_data():
    with open("data/models.json", "r") as f:
        data = json.load(f)

    db = Session(database.SessionLocal())

    for entry in data:
        brand = models.Brand(name=entry["brand_name"], average_price=0)
        db.add(brand)
        db.commit()
        db.refresh(brand)

        model = models.Model(
            name=entry["name"], average_price=entry["average_price"], brand_id=brand.id)
        db.add(model)
        db.commit()

    db.close()
