
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String, nullable=False)
    email = db.Column (db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)



    def __init__(self,  username, city, email,password):
        
        self.username = username
        self.city= city
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()  



class EventPost(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    img_url=db.Column(db.String, nullable=False) 
    caption = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)  
    date =  db.Column(db.DateTime, default=datetime.utcnow(),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False )  

    def  __init__(self, img_url, caption, location, user_id):
        self.img_url = img_url
        self.caption = caption
        self.location = location
        self.user_id = user_id




    def save(self):
        db.session.add(self)
        db.session.commit()     