from flask import Blueprint, render_template
from models.index import db
languages_blueprint = Blueprint('languages', __name__, url_prefix='/languages')

@languages_blueprint.route('/')
def index():
    langs = {}
    characters = list(db.characters.find())
    for c in characters:
        for l in c['languages']:
            if l in langs:
                langs[l].append(c['name'])
            else:
                # Make a list with character name in it assigned to the language
                langs[l] = [c['name']]
    return render_template('languages/index.html', langs=langs)