from flask import Flask
from main import main
from chart import chart
from data import data
from search import search
from models import db,About

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///about.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret-key"

db.init_app(app)

app.register_blueprint(main)
app.register_blueprint(chart)
app.register_blueprint(data)
app.register_blueprint(search)
