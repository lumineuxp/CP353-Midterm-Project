from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()

class About(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(), nullable=False)
   image = db.Column(db.String(), nullable=False)