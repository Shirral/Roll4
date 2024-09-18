import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
# if os.path.exists(".env"):
from dotenv import load_dotenv
load_dotenv()


print("MONGO_URI:", os.environ.get("MONGO_URI"))  # Debugging statement
print("DB_URL:", os.environ.get("DB_URL"))  # Debugging statement

app = Flask(__name__)

# Configuration
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
app.secret_key = os.environ.get("SECRET_KEY")

# Initialize MongoDB and SQLAlchemy
mongo = PyMongo(app)
db = SQLAlchemy(app)

# Import routes
from roll4app import routes