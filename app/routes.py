from app import app, db
from flask import render_template, request, redirect, url_for
from app.forms import HousesForm
from app.models import Houses

# http://0.0.0.0:5000/

@app.route('/')
@app.route('/index')
@app.route('/hello')
def index():
    return "Hello World!"


@app.route('/staff')
def staff():
    staffmembers = [{'name': 'Olivier', 'email': 'olivier@claerbout.eu'},
                    {'name': 'Titus', 'email': 'titus@claerbout.eu'},
                    {'name': 'Joke', 'email': 'joke@claerbout.eu'}]
    return render_template('staff.html', staffmembers=staffmembers)


@app.route('/house/overview', methods=['GET', 'POST'])
def houseoverview():
    houses = Houses.query.all()
    return render_template('houses_list.html', houses=houses)


@app.route('/house/add', methods=['POST', 'GET'])
def house_insert():
    form = HousesForm()
    if form.validate_on_submit():
        new_house = Houses(longitude=form.longitude.data,
                           latitude=form.latitude.data,
                           housing_median_age=form.housing_median_age.data,
                           total_rooms=form.total_rooms.data,
                           total_bedrooms=form.total_bedrooms.data,
                           population=form.population.data,
                           households=form.households.data,
                           median_income=form.median_income.data,
                           median_house_value=form.median_house_value.data,
                           ocean_proximity=form.ocean_proximity.data)
        db.session.add(new_house)
        db.session.commit()
        return redirect(url_for('houseoverview'))
    return render_template('house_add.html', form=form, title='Voeg huis toe')
