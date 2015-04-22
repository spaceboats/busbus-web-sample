import flask
from flask import jsonify
from collections import deque

app = flask.Flask(__name__)

author = "Nick, Monica, Alex"

@app.route('/')
def home():
    name = "Home"
    return flask.render_template('index.html', author=author, name=name)

@app.route('/datastream')
def datastream():
    name = "Datastream"
    return flask.render_template('datastream.html', author=author, name=name)

@app.route('/search')
def search():
    name = "Search"
    return flask.render_template('search.html', author=author, name=name)

@app.route('/searchAgency')	
def searchAgency():
	name = "SearchAgency"
	return flask.render_template('searchAgency.html', author=author, name=name)

if __name__ == '__main__':
    app.run(debug=True)
