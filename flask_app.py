
# A very simple Flask Hello World app for you to get started with...
import constants
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Joel!'

@app.route('/aboutme')
@app.route('/about me')
def about_me():
    return app.send_static_file('about me.html')

@app.route('/class_schedule')
def class_schedule():
    return render_template('class_schedule.html',
                           courses=constants.COURSES)


@app.route('/register')
def register():
    return app.send_static_file('register.html')