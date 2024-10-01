from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from roll4app import app, mongo, db
from roll4app.models import Users


@app.route("/")
@app.route("/lists")
def lists():
    if "currentuser" in session:

        d20 = list(mongo.db.Lists.find({"Die": 20, "UserName": session["currentuser"]}))
        d12 = list(mongo.db.Lists.find({"Die": 12, "UserName": session["currentuser"]}))
        d10 = list(mongo.db.Lists.find({"Die": 10, "UserName": session["currentuser"]}))
        d8 = list(mongo.db.Lists.find({"Die": 8, "UserName": session["currentuser"]}))
        d6 = list(mongo.db.Lists.find({"Die": 6, "UserName": session["currentuser"]}))
        d4 = list(mongo.db.Lists.find({"Die": 4, "UserName": session["currentuser"]}))

        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        if "currentuser" in session:
            return render_template("lists.html", sessioncookie = True, d20=d20, d12=d12, d10=d10, d8=d8, d6=d6, d4=d4, darkmode=darkmode)
        else:
            return render_template("lists.html", sessioncookie = False, d20=d20, d12=d12, d10=d10, d8=d8, d6=d6, d4=d4, darkmode=darkmode)

    return redirect(url_for("notloggedin"))

@app.route("/userprofile", defaults={"username": None}, methods=["GET", "POST"])
@app.route("/userprofile/", defaults={"username": None}, methods=["GET", "POST"])
@app.route("/userprofile/<username>", methods=["GET", "POST"])
def userprofile(username):
    if "currentuser" in session:
        if username == None:
            username = session["currentuser"]

        user = Users.query.filter_by(user_name=session["currentuser"]).first()
        username = user.user_name
        darkmode = user.darkmode

        if request.method == "POST":
            user.darkmode = bool(True if request.form.get("darkmode") else False)
            db.session.commit()
            return redirect(url_for("userprofile"))      
        
        return render_template("userprofile.html", username=username, user=user, darkmode=darkmode)
    
    return redirect(url_for("notloggedin"))
   

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
        return redirect(url_for("userprofile", username=session["currentuser"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = Users.query.filter_by(user_name=request.form.get("user_name").lower()).first()

        if existing_user:
            if check_password_hash(existing_user.user_password, request.form.get("user_password")):
                session['currentuser'] = request.form.get("user_name").lower()
                flash(f"Hello again, {session['currentuser']}! Ready to roll?")
                return redirect(url_for("lists"))

            else:
                flash("Hmm... something's incorrect here. Try again!")
                return redirect(url_for("login"))
            
        else:
            flash("Hmm... something's incorrect here. Try again!")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    if "currentuser" in session:
        flash("Logged out. See you later!")
        session.pop("currentuser")
        return redirect(url_for("login"))
    return render_template("notloggedin.html")


@app.route("/addlist", defaults={"die": None})
@app.route("/addlist/", defaults={"die": None})
@app.route("/addlist/<int:die>", methods=["GET", "POST"])
def addlist(die):
    if "currentuser" in session:
        categories = mongo.db.Categories.find()
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        if die == None:
            return redirect(url_for("newlist"))

        if request.method == "POST":
            newlist = {
                "ListName": request.form.get("list_name"),
                "Die": die,
                "Category": request.form.get("category"),
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
            return redirect(url_for("lists"))

        return render_template("addlist.html", die=die, categories=categories, darkmode=darkmode)

    return redirect(url_for("notloggedin"))


@app.route("/editlist", defaults={"listid": None})
@app.route("/editlist/", defaults={"listid": None})
@app.route("/editlist/<listid>", methods=["GET", "POST"])
def editlist(listid):
    if "currentuser" in session:

        userlist = mongo.db.Lists.find_one({"_id": ObjectId(listid)})
        categories = mongo.db.Categories.find()
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        if listid == None:
            return redirect(url_for("lists"))
        
        if not userlist:
                flash("List not found!")
                return redirect(url_for("lists"))

        if session["currentuser"].lower() != userlist["UserName"].lower():
            flash("Oops! You were taken some strange places. It's okay, we've got you back here now!")
            return redirect(url_for("lists"))

        if request.method == "POST":
                editedlist = {
                    "ListName": request.form.get("list_name"),
                    "Category": request.form.get("category"),
                    "ListItems": {},
                    "ListItemNotes": {}
                }

                num = 1
                for key, val in request.form.items():
                    if key.startswith("listitem"):
                        editedlist["ListItems"][str(num)] = val
                        num += 1

                num2 = 1
                for key, val in request.form.items():
                    if key.startswith("linote"):
                        editedlist["ListItemNotes"][str(num2)] = val
                        num2 += 1

                mongo.db.Lists.update_one({"_id": ObjectId(listid)}, {"$set": editedlist})
                flash("List updated!")
                return redirect(url_for("listview", listid = listid, userlist=userlist, darkmode=darkmode))

        return render_template("editlist.html", listid = listid, userlist=userlist, categories=categories, darkmode=darkmode)

    return redirect(url_for("notloggedin"))


@app.route("/deletelist", defaults={"listid": None})
@app.route("/deletelist/", defaults={"listid": None})
@app.route("/deletelist/<listid>")
def deletelist(listid):
    if "currentuser" in session:

        if listid == None:
            return redirect(url_for("lists"))
        
        mongo.db.Lists.delete_one({"_id": ObjectId(listid)})
        flash("List deleted!")
        return redirect(url_for("lists"))

    return redirect(url_for("notloggedin"))


@app.route("/listview", defaults={"listid": None})
@app.route("/listview/", defaults={"listid": None})
@app.route("/listview/<listid>", methods=["GET", "POST"])
def listview(listid):
    if "currentuser" in session:
    
        userlist = mongo.db.Lists.find_one({"_id": ObjectId(listid)})
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        if listid == None:
            return redirect(url_for("lists"))
        
        if not userlist:
                flash("List not found!")
                return redirect(url_for("lists"))

        if session["currentuser"].lower() != userlist["UserName"].lower():
            flash("Oops! You were taken some strange places. It's okay, we've got you back here now!")
            return redirect(url_for("lists"))

        return render_template("listview.html", listid = listid, userlist=userlist, darkmode=darkmode)

    return redirect(url_for("notloggedin"))


@app.route("/newlist")
def newlist():
    if "currentuser" in session:
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode
        return render_template("newlist.html", darkmode=darkmode)

    return redirect(url_for("notloggedin"))


@app.route("/categories")
def categories():
    if "currentuser" in session:
        categories = mongo.db.Categories.find()
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        return render_template("categories.html", categories=categories, darkmode=darkmode)

    return redirect(url_for("notloggedin"))


@app.route("/addcategory", methods=["GET", "POST"])
def addcategory():
    if "currentuser" in session:
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        if request.method == "POST":
            newcategory = {
                "CategoryName": request.form.get("category_name"),
                "UserName": session['currentuser'],
                "CategoryColour": request.form.get("colour")
            }

            mongo.db.Categories.insert_one(newcategory)
            flash("Category created! You can now choose it from the 'Add category?' dropdown menu while creating/editing a list.")
            return redirect(url_for("categories"))

        return render_template("addcategory.html", darkmode=darkmode)

    return redirect(url_for("notloggedin"))


@app.route("/editcategory", defaults={"categoryid": None})
@app.route("/editcategory/", defaults={"categoryid": None})
@app.route("/editcategory/<categoryid>", methods=["GET", "POST"])
def editcategory(categoryid):
    if "currentuser" in session:

        if categoryid == None:
            return redirect(url_for("categories"))
        
        category = mongo.db.Categories.find_one({"_id": ObjectId(categoryid)})
        darkmode = Users.query.filter_by(user_name=session["currentuser"]).first().darkmode

        if not category:
            flash("Category not found!")
            return redirect(url_for("categories"))

        if session["currentuser"].lower() != category["UserName"].lower():
            flash("Oops! You were taken some strange places. It's okay, we've got you back here now!")
            return redirect(url_for("categories"))
        
        if request.method == "POST":

            editedcategory = {
                "CategoryName": request.form.get("category_name"),
                "CategoryColour": request.form.get("colour")
            }

            mongo.db.Categories.update_one({"_id": ObjectId(categoryid)}, {"$set": editedcategory})
            
            flash("Category Updated!")
            return redirect(url_for("categories"))

        return render_template("editcategory.html", category=category, categoryid=categoryid, darkmode=darkmode)

    return redirect(url_for("notloggedin"))  


@app.route("/deletecategory", defaults={"categoryid": None})
@app.route("/deletecategory/", defaults={"categoryid": None})
@app.route("/deletecategory/<categoryid>")
def deletecategory(categoryid):
    if "currentuser" in session:

        if categoryid == None:
                return redirect(url_for("categories"))
        
        mongo.db.Categories.delete_one({"_id": ObjectId(categoryid)})
        flash("Category deleted!")
        return redirect(url_for("categories"))

    return redirect(url_for("notloggedin"))

@app.route("/deleteuser/<username>")
def deleteuser(username):
    if "currentuser" in session:

        user = Users.query.filter_by(user_name=username).first_or_404()
        db.session.delete(user)
        db.session.commit()

        if session["currentuser"].lower() != username.lower():
            flash("Oops! You were taken some strange places. It's okay, we've got you back here now!")
            return redirect(url_for("lists"))

        flash("Profile deleted. See ya!")
        return redirect(url_for("login"))

    return redirect(url_for("notloggedin"))

@app.route("/notloggedin")
def notloggedin():
    if "currentuser" in session:
        return redirect(url_for("lists"))
    
    return render_template("notloggedin.html")