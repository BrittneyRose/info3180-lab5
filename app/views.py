"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This poster creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_poster
import os
from app.forms import MovieForm
from werkzeug.utils import secure_postername
from app.models import Movie
from flask import send_from_directory
from . import db
from app.config import Config
UPLOAD_FOLDER = Config.UPLOAD_FOLDER


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
@app.route('/api/v1/movies/', methods=['POST'])
def create():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        filename = secure_filename(poster.filename)
        destination_folder = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
        os.makedirs(destination_folder, exist_ok=True)
        poster.save(os.path.join(app.root_path, UPLOAD_FOLDER, filename))

        created_at=created_at

        movies = Movie(
            title=title,
            description=description,
            poster=poster,
            created_at=created_at
        )
        db.session.add(movies)
        db.session.commit()

        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 201
    else:
        return jsonify(errors=form_errors(form)), 400
        
 


def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<poster_name>.txt')
def send_text_poster(poster_name):
    """Send your static text poster."""
    poster_dot_text = poster_name + '.txt'
    return app.send_static_poster(poster_dot_text)


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