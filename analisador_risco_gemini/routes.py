from flask import current_app as app
from flask import render_template, request


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
