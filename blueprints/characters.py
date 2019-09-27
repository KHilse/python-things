from flask import Blueprint, render_template, request, redirect
from datetime import datetime

character_blueprint = Blueprint('characters', __name__, url_prefix='/characters')

@character_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('characters/index.html')
    elif request.method == 'POST':
        name = request.form['name']
        print('you entered the name:', name)
        langs = request.form['languages'].split(',')
        print('langs:', langs)
        formatted_langs = [x.strip() for x in langs]
        if request.form['birthday']:
            formatted_date = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
        else:
            formatted_date = None
        print('formatted_date:', formatted_date)
        return redirect('/characters')
