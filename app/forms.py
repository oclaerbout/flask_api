from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import app, db
from app.models import Houses

class HousesForm(FlaskForm):
    longitude = FloatField('Longitude', validators=[DataRequired()])
    latitude = FloatField('Latitude')
    housing_median_age = FloatField('Median Age')
    total_rooms = FloatField('Total Rooms')
    total_bedrooms = FloatField('Total Bedrooms')
    population = FloatField('Population')
    households = FloatField('Households')
    median_income = FloatField('Median Income')
    median_house_value = FloatField('Median House Value')
    ocean_proximity = StringField('Ocean Proximity')
    submit = SubmitField('Process housing data')


