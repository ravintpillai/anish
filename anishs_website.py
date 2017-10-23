<!doctype html>
<html>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-107714833-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-107714833-1');
</script>


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
	return "This fabulous website was made by a person, who got the domain as a gift from an epic guy..."

@app.route('/contact')
def contact_thing():
	return "I am impossible to contact. Sadly. But, if you know how to navigate the internet, you can find me..."

if __name__ == '__main__':
 	app.debug = True
 	port = int(os.environ.get("PORT", 5000))
 	app.run(host='0.0.0.0', port=port)
