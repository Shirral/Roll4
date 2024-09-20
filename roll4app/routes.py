from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
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
        existing_user = Users.query.filter_by(user_name=request.form.get("user_name").lower()).first()

        if existing_user:
            flash("Username already taken. Sorry!") #change flash to sth nicer later
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("user_name").lower(),
            user_password=generate_password_hash(request.form.get("user_password")))
        db.session.add(user)
        db.session.commit()

        session["currentuser"] = request.form.get("user_name").lower()
        flash(f"Welcome onboard, {session['currentuser']}!")
        return redirect(url_for("userprofile"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = Users.query.filter_by(user_name=request.form.get("user_name").lower()).first()

        if existing_user:
            if check_password_hash(existing_user.user_password, request.form.get("user_password")):
                session['currentuser'] = request.form.get("user_name").lower()
                flash(f"Hello again, {session['currentuser']}! Ready to roll?")
                return redirect(url_for("list_view"))

            else:
                flash("Hmm... something's incorrect here. Try again!")
                return redirect(url_for("login"))
            
        else:
            flash("Hmm... something's incorrect here. Try again!")
            return redirect(url_for("login"))

    return render_template("login.html")
