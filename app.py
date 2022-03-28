import flask
import requests
import os

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

math_solution = 2+2

@app.route("/")
def index():
    return flask.render_template("index.html", solution=math_solution)


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)