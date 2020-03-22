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
    fsm_json = request.form['fsm_json']
    deterministic = request.form['deterministic']
    if deterministic == 'true':
        det = True
    else:
        det = False
    return fsm_json + "\n" + FSM.parse_json(fsm_json, det)


if __name__ == "__main__":
    app.run(debug=True)
