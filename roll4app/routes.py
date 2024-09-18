from flask import render_template, request
from roll4app import app, mongo, db

@app.route("/")
@app.route("/list_view")
def list_view():
    lists = mongo.db.Lists.find()
    return render_template("lists.html", lists=lists)