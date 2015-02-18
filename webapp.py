import flask
app = flask.Flask(__name__)

@app.route('/')
def home():
    author = "Nick, Monica"
    name = "Home"
    return flask.render_template('index.html', author=author, name=name)

@app.route('/datastream')
def datastream():
    author = "Nick, Monica"
    name = "Datastream"
    return flask.render_template('datastream.html', author=author, name=name)

if __name__ == '__main__':
    app.run(debug=True)
