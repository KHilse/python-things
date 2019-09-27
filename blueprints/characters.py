from flask import Blueprint, render_template, request, redirect
from datetime import datetime
from bson.objectid import ObjectId
from models.index import db

character_blueprint = Blueprint('characters', __name__, url_prefix='/characters')

@character_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        characters = list(db.characters.find())
        return render_template('characters/index.html', characters=characters)
    elif request.method == 'POST':
        langs = [x.strip() for x in request.form['languages'].split(',')]
        if request.form['birthday']:
            formatted_date = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
        else:
            formatted_date = None
        db.characters.insert_one({
            "name": request.form['name'],
            'image': request.form['image'],
            'birthday': formatted_date,
            'languages': langs,
            'bio': request.form['bio']
        })
        return redirect('/characters')

@character_blueprint.route('/<char_id>')
def show(char_id):
    character = db.characters.find_one({'_id': ObjectId(char_id)})
    return render_template('characters/show.html', character=character)