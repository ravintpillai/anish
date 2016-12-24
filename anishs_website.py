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

 if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)
