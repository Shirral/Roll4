from flask import render_template, request
from roll4app import app, mongo, db
from roll4app.models import Users

@app.route("/")
@app.route("/list_view")
def list_view():
    lists = mongo.db.Lists.find()
    return render_template("lists.html", lists=lists)