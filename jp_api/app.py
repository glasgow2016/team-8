#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hey! Human"

@app.route('/map')
def get_map():
    return 'map here'

@app.route('/ranking')
def get_rank():
    return 'rank here'

@app.route('/sensor')
def sensor():
    return 'sensor'

if __name__ == '__main__':
    app.run(debug=True)
