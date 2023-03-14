"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

import os
from app import app
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from app.forms import Add_New_Property_Form
from app.models import Profile_Property
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/properties/create', methods = ['POST', 'GET'])
def create():

    form = Add_New_Property_Form()

    if request.method == "POST":
        if form.validate_on_submit:
           Type = request.form['Type']
           Photo = request.form['Photo']
           Title_of_Property = request.form['Title_of_Property']
           Number_of_Bedrooms = request.form['Number_of_Bedrooms']
           Number_of_Bathrooms = request.form['Number_of_Bathrooms']
           Location = request.form['Location']
           Price = request.form['Price']
           Description = request.form['Description']

           filename = secure_filename(Photo.filenmae)
           Photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

           enter = Profile_Property(Type, Title_of_Property, Number_of_Bedrooms, Number_of_Bathrooms, Location, Price, Description)
           flash('File Upload Successfully')
           db.session.add(enter)
           db.session.commit

           return redirect(url_for('properties.html'))


    return render_template('create.html', form=form)

@app.route('/properties')
def properties():
    properties = db. session.execute(db.select(Profile_Property)).scalars()
    return render_template('properties.html', properties = properties)

@app.route('/properties/<property_id>')
def propertyid(property_id):
    property_id = int(property_id)
    estate = db.session.execute(db.select(Profile_Property).filter_by(id=property_id).scalar_one)
    return render_template('propertyid.html', property = estate)

def get_images():
    rootdir = os.getcwd()
    filelist=[]

    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            filelist.append(file)
        return filelist
    
@app.route('/upload/<filenmae>')
def get_uploaded_images(filename):
    rootdir = os.getcwd()
    return send_from_directory(os.path.join(rootdir,app.config['UPLOADED_FOLDER']), filename)


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Real Estate")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404