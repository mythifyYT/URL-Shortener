from flask import Flask, render_template, request, redirect
import random
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home_page():
	letters = open('letters.txt').read().split()
	random_url = f"{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}"
	
	
	if request.method == "POST":
		url = request.form['url']
		print(url)
		with open('urls.json', 'r') as f:
		    urls = json.load(f)
		
		urls[random_url] = url

		with open('urls.json', 'w') as f:
		    json.dump(urls, f, indent=4)
		return render_template('index.html', short=random_url)
	
	return render_template('index.html')



@app.route('/<redirect_short>')
def redir(redirect_short):
	with open('urls.json', 'r') as f:
		urls = json.load(f)
	
	
	return redirect(urls[redirect_short])


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)