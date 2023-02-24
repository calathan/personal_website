import flask

app = flask.Flask(__name__)

app.config['DEBUG'] = True

@app.route("/bogus", methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1 <p>This site is a proptotype API for things.</p>"