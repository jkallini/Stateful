from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/postmethod', methods=['POST'])
def get_post_javascript_data():
	jsdata = request.form['javascript_data']
	json.loads(jsdata)
	print(jsdata)
	return jsdata


if __name__ == "__main__":
    app.run(debug=True)
