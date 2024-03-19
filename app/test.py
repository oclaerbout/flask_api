from app import app, db
from app.models import Houses
import sqlalchemy as sa

house = Houses(
            longitude=-122.23,
            latitude=37.88,
            housing_median_age=41.0,
            total_rooms=880.0,
            total_bedrooms=129.0,
            population=322.0,
            households=126.0,
            median_income=8.3252,
            median_house_value=452600.0,
            ocean_proximity='NEAR BAY'
)

with app.app_context():
    db.session.add(house)
    db.session.commit()