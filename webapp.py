import flask
import time
import string
import random
from flask import jsonify
from collections import deque

app = flask.Flask(__name__)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class Struct:
    route = ""
    city = ""
    onTime = ""

@app.route('/')
def home():
    author = "Nick, Monica"
    name = "Home"
    return flask.render_template('index.html', author=author, name=name)

@app.route('/deletelater')
def fakeData():
    dataDic = [ { "time": 123123123123, "departure_time": 123123123123, "headsign": "to Daisy Hill", "stop": { "id": "idStop", "code": "codeStop", "name": "nameStop1" }, "route": { "agency": { "id": "idAgency", "name": "nameAgency1", "url": "urlAgency" }, "id": "idRoute", "short_name": "nameRoute1" } }, 
                { "time": 123123123123, "departure_time": 123123123123, "headsign": "to Daisy Hill", "stop": { "id": "idStop", "code": "codeStop", "name": "nameStop2" }, "route": { "agency": { "id": "idAgency", "name": "nameAgency2", "url": "urlAgency" }, "id": "idRoute", "short_name": "nameRoute2" } }, 
                { "time": 123123123123, "departure_time": 123123123123, "headsign": "to Daisy Hill", "stop": { "id": "idStop", "code": "codeStop", "name": "nameStop3" }, "route": { "agency": { "id": "idAgency", "name": "nameAgency3", "url": "urlAgency" }, "id": "idRoute", "short_name": "nameRoute3" } }, 
                { "time": 123123123123, "departure_time": 123123123123, "headsign": "to Daisy Hill", "stop": { "id": "idStop", "code": "codeStop", "name": "nameStop4" }, "route": { "agency": { "id": "idAgency", "name": "nameAgency4", "url": "urlAgency" }, "id": "idRoute", "short_name": "nameRoute4" } }, 
                { "time": 123123123123, "departure_time": 123123123123, "headsign": "to Daisy Hill", "stop": { "id": "idStop", "code": "codeStop", "name": "nameStop5" }, "route": { "agency": { "id": "idAgency", "name": "nameAgency5", "url": "urlAgency" }, "id": "idRoute", "short_name": "nameRoute5" } } ]
    return flask.json.jsonify(arrivals = dataDic)


@app.route('/datastream')
def datastream():
    author = "Nick, Monica"
    name = "Datastream"

    theTime = time.asctime( time.localtime( time.time() ) )
        
    return flask.render_template('datastream.html', author=author, name=name, theTime=theTime)

@app.route('/search')
def search():
    author = "Nick, Monica"
    name = "Search"

    return flask.render_template('search.html', author=author, name=name)


if __name__ == '__main__':
    app.run(debug=True)
