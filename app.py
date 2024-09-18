import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from bson.objectid import ObjectId
from models import Users
if os.environ.get("DEVELOPMENT") == True:
    from dotenv import load_dotenv
    load_dotenv()


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
db = SQLAlchemy(app)


print("Connected to database:", mongo.db)  # Check if db is None

@app.route("/")
@app.route("/list_view")
def list_view():
    
    lists = mongo.db.Lists.find()
    return render_template("lists.html", lists = lists)
 

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)