from flask import Blueprint, render_template,request
from urllib.request import urlopen
from urllib.parse import quote
import json
from chart import chTrack
from models import db,About
main = Blueprint('main', __name__)

@main.route('/')
def index():
    cTrack = chTrack()
    return render_template('index.html',tracks = cTrack)

@main.route('/about')
def about():
   # return render_template('about.html', students = About.query.all() )
   return render_template('about.html', students = About.query.all() )

