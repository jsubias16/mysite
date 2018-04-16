
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

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
    return app.send_static_file('Class schedule.html')

@app.route('/register')
def register():
    return app.send_static_file('register.html')