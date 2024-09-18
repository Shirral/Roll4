from app import db


#schema for the PostreSQL database "roll4users" containing the "Users" table
#with the user data
class Users(db.model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False, unique=True)
    user_password = db.Column(db.String(30), nullable=False)
    darkmode = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"Username: {self.user_name},\nPassword: {self.user_password},\nDark mode: {self.darkmode}"
