# Imports
from flask import Flask, render_template
from blueprints.characters import character_blueprint
from blueprints.languages import languages_blueprint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

# Blueprints (controllers)
app.register_blueprint(character_blueprint)
app.register_blueprint(languages_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

