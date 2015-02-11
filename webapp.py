import flask
app = flask.Flask(__name__)

@app.route('/')
def not_hello_world():
    author = "Nick"
    name = "Home?"
    return flask.render_template('index.html', author=author, name=name)

if __name__ == '__main__':
    app.run(debug=True)
