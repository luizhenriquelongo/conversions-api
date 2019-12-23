from app import app
from db.dao import MongoDao
from datetime import datetime, date
from flask import (
    render_template, request, 
    make_response, jsonify, 
    flash, redirect, url_for
)


@app.route('/', methods=['GET', ])
def index():
    return render_template('form.html', titulo='Conversions API')


@app.route('/api/v1/add_conversion', methods=['POST', ])
def add_conversion():
    dao = MongoDao(request.form['email'])
    material = {"material": request.form['material']}
    new_document = {
        "email": request.form['email'],
        "telefone": request.form['telefone'],
        "cargo": request.form['cargo'],
        "created": datetime.now(),
    }       

    dao.insert_document(new_document, material)
    flash('Document Created!')
    return redirect(url_for('index')) 

regex_date = "<regex('\d{2}-\d{2}-\d{4}')"

@app.route('/api/v1/conversions/', methods=['GET', ])
def show_all():
    response = MongoDao.get_all()
    return make_response(response, 200)

@app.route(f"/api/v1/conversions/{regex_date}:initial_date>/{regex_date}:final_date>", methods=['GET', ])
def conversions(initial_date, final_date):
    try:
        initial_date = datetime.strptime(initial_date, '%d-%m-%Y')
        final_date = datetime.strptime(final_date, '%d-%m-%Y')
        if final_date > datetime.now():
            raise ValueError
    except ValueError:
        error = {
            "error": "Please verify and make sure that the date passed is correct!"}
        return make_response(jsonify(error), 400)

    else:
        if initial_date > final_date:
            initial_date, final_date = final_date, initial_date
        if final_date.date() == datetime.now().date():
            final_date = datetime.now()

        contacts_created_count = MongoDao.get_contacts_created_count(
            initial_date, final_date)
        contacs_with_conversions = MongoDao.get_contacts_with_no_empty_conversions_count(
            initial_date, final_date)
        contacts_count_segmented_by_material = MongoDao.get_segmented_conversions_count(
            initial_date, final_date)

        response = {
            "response": {
                "createdContatcs": contacts_created_count,
                "contactsWithAtLeastOneConversion": contacs_with_conversions,
                "contactsSegmentedByMaterial": contacts_count_segmented_by_material
            }
        }

        return make_response(jsonify(response), 200)
