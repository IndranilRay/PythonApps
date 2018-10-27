from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index_deprecated():
# 	# return index page
# 	title = "Indranil Ray - Full Stack Developer"
# 	return render_template('index.html', title=title)

@app.route('/')
def index():
	return render_template('profile.html')


if __name__ == '__main__':
	app.run(debug=True)

