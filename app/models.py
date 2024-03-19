from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Houses(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    longitude: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    latitude: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    housing_median_age: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    total_rooms: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    total_bedrooms: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    population: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    households: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    median_income: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    median_house_value: so.Mapped[float] = so.mapped_column(sa.Float, default=0.0, nullable=True)
    ocean_proximity: so.Mapped[str] = so.mapped_column(sa.String(256))

    def __repr__(self) -> str:
        return f"<Houses {self.id}>"


