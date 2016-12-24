from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is Anishs First Website'

@app.route('/anish_related_things')
def anish_related_things():
	return "Hi, I am related to Anish, obviously"

@app.route('/shenanigans/more')
def other_thing():
	return "Hi, I am more shenanigans"
