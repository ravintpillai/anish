from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Anish is the ruler and nobody will find this'

@app.route('/anish_related_things')
def anish_related_things():
	return "This program made on GitHub is related to the guy sometimes known as Anish Mariathasan"

@app.route('/about')
def other_thing():
	return "This fabulous website was made by a person who got the domain as a gift from an epic guy"

@app.route('/contact')
def contact_thing():
	return "I am impossible to contact"

if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)
