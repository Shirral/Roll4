from flask import render_template, request, redirect, url_for
from roll4app import app, mongo, db
from roll4app.models import Users

@app.route("/")
@app.route("/list_view")
def list_view():
    lists = mongo.db.Lists.find()
    return render_template("lists.html", lists=lists)

@app.route("/userprofile")
def userprofile():
    user = list(Users.query.all())
    return render_template("userprofile.html", user=user)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users(
            user_name=request.form.get("user_name"),
            user_password=request.form.get("user_password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("userprofile"))
    return render_template("register.html")
