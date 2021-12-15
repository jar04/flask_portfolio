# import "packages" from flask
from flask import Flask, render_template, request, json
import requests

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/aboutnathan')
def aboutnathan():
    return render_template("aboutnathan.html")

@app.route('/aboutreem')
def aboutreem():
    return render_template("aboutreem.html")


@app.route('/aboutjacob')
def aboutjacob():
    return render_template("aboutjacob.html")


@app.route('/aboutjames')
def aboutjames():
    return render_template("aboutjames.html")


@app.route('/aboutdaniel')
def aboutdaniel():
    return render_template("aboutdaniel.html")


@app.route('/mainabout/')
def mainabout():
    return render_template("mainabout.html")

@app.route('/feedback/', methods=['GET', 'POST'])
def feedback():
    if request.form:
        input = request.form.get("feed1")
        name = request.form.get("feed2")
        if len(input) != 0:  # input field has content
            return render_template("layouts/feedback.html", input=input, name=name)
    return render_template("layouts/feedback.html")

@app.route('/translator/', methods=['GET', 'POST'])
def translator():
    if request.form:
        input = request.form.get("feed1")
        name = request.form.get("feed2")
        if len(input) != 0:  # input field has content
            return render_template("layouts/translator.html", input=input, name=name)
    return render_template("layouts/translator.html")


# runs the application on the development server
# changed port from 5000 to 8080 to test gunicorn
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
