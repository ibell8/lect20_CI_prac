import flask
import requests
import os

app = flask.Flask(__name__)

math_solution = 2+2

@app.route("/")
def index():
    return flask.render_template("index.html", solution=math_solution)


app.run()