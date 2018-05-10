
# A very simple Flask Hello World app for you to get started with...
from flask import Flask
from flask import render_template
import constants
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object('config.BaseConfig')
db = SQLAlchemy(app)
Bootstrap(app)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.Integer)
    name = db.Column(db.String(80))
    teacher_name = db.Column(db.String(80))
    resource_name = db.Column(db.String(80))
    resource_url = db.Column(db.String(300))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    artist_name = db.Column(db.String(80))
    youtube_url = db.Column(db.String(300))

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('aboutme.html')


@app.route('/class_schedule')
def class_schedule():
    courses = Course.query.all()
    return render_template('class_schedule.html',
                           courses=courses)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/top_ten_songs')
def top_ten_songs():
    songs = Song.query.all()
    return render_template('top_ten_songs.html',
                           songs=songs)

if __name__ == '__main__':
  db.create_all()