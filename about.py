from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///about.db'

db = SQLAlchemy(app)

class About(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(), nullable=False)
   image = db.Column(db.String(), nullable=False)
   
@app.route('/')
def about():
   return render_template('about.html', students = About.query.all() )

