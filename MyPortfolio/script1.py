from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	# return index page
	title = "Indranil Ray - Full Stack Developer"
	return render_template('index.html', title = title)


@app.route('/home')
def home():
	# return "Home page content goes here!!"
	return render_template('home.html')


@app.route('/about/')
def about():
	# return "About us content goes here"
	return render_template('about.html')


if __name__ == '__main__':
	app.run(debug=True)

