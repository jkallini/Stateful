from flask import Flask, render_template, url_for, request
import fsm as FSM

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/fsmreceiver', methods=['POST'])
def fsmreceiver():
	jsdata = request.form['javascript_data']
	FSM.parse_json(jsdata)
	return jsdata


if __name__ == "__main__":
    app.run(debug=True)
