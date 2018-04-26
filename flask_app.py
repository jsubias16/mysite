
# A very simple Flask Hello World app for you to get started with...
import constants
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/aboutme')
@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                           courses=constants.COURSES)


@app.route('/register')
def register():
    return render_template('register.html')