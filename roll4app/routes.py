from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from roll4app import app, mongo, db
from roll4app.models import Users

@app.route("/")
@app.route("/list_view")
def list_view():
    d20 = list(mongo.db.Lists.find({"Die": 20}))
    d12 = list(mongo.db.Lists.find({"Die": 12}))
    d10 = list(mongo.db.Lists.find({"Die": 10}))
    d8 = list(mongo.db.Lists.find({"Die": 8}))
    d6 = list(mongo.db.Lists.find({"Die": 6}))
    d4 = list(mongo.db.Lists.find({"Die": 4}))

    if "currentuser" in session:
        return render_template("lists.html", sessioncookie = True, d20=d20, d12=d12, d10=d10, d8=d8, d6=d6, d4=d4)
    else:
        return render_template("lists.html", sessioncookie = False, d20=d20, d12=d12, d10=d10, d8=d8, d6=d6, d4=d4)

@app.route("/userprofile", defaults={"username": None}, methods=["GET", "POST"])
@app.route("/userprofile/", defaults={"username": None}, methods=["GET", "POST"])
@app.route("/userprofile/<username>", methods=["GET", "POST"])
def userprofile(username):
    if "currentuser" in session:
        if username == None:
            username = session["currentuser"]
            
        username = Users.query.filter_by(user_name=session["currentuser"]).first().user_name
        return render_template("userprofile.html", username=username)
    
    flash("You must be logged in to view this page!")
    return redirect(url_for("login"))
   

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
        return redirect(url_for("userprofile"), username=session["currentuser"])
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


@app.route("/logout")
def logout():
    flash("Logged out. See you later!")
    session.pop("currentuser")
    return redirect(url_for("login"))


@app.route("/addlist/<int:die>", methods=["GET", "POST"])
def addlist(die):
    if "currentuser" in session:
        if request.method == "POST":
            newlist = {
                "ListName": request.form.get("list_name"),
                "Die": die,
                "UserName": session['currentuser'],
                "ListItems": {},
                "ListItemNotes": {}
            }

            num = 1
            for key, val in request.form.items():
                if key.startswith("listitem"):
                    newlist["ListItems"][str(num)] = val
                    num += 1

            num2 = 1
            for key, val in request.form.items():
                if key.startswith("linote"):
                    newlist["ListItemNotes"][str(num2)] = val
                    num2 += 1

            mongo.db.Lists.insert_one(newlist)
            flash("List created. Woohoo!")
            return redirect(url_for("list_view"))

        return render_template("addlist.html", die=die)

    flash("You must be logged in to view this page!")
    return redirect(url_for("login"))

@app.route("/newlist")
def newlist():
    if "currentuser" in session:
        return render_template("newlist.html")
    
    flash("You must be logged in to view this page!")
    return redirect(url_for("login"))
