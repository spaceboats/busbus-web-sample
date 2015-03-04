import flask
import time
import string
import random
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

@app.route('/datastream')
def datastream():
    author = "Nick, Monica"
    name = "Datastream"

    while True:
	s1 = Struct()
        theTime = time.asctime( time.localtime( time.time() ) )
        s1.route = id_generator()
        s1.city = id_generator()
        s1.onTime = id_generator()
        return flask.render_template('datastream.html', author=author, name=name, theTime=theTime, s1=s1)
        time.sleep(10)

if __name__ == '__main__':
    app.run(debug=True)
