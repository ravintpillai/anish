from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
	


@app.route('/anish_related_things')
def anish_related_things():
	return "This program made on GitHub, is related to the guy sometimes known as Anish Mariathasan."

@app.route('/about')
def other_thing():
	return "Hello! If you found this by a general search, you will know that I edit Wikipedia (constructively!) and Q & A forums like Quora and StackOverflow. Anyway, um...everything else you could possibly want to know can be found by searching."
	

@app.route('/contact')
def contact_thing():
	return "I am impossible to contact. Sadly. But, if you know how to navigate the internet, you can find me..."

@app.route('/play')
def fun_thing():
	return render_template('contact.html')

if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)
	

