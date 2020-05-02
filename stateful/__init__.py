from flask import Flask

app = Flask(__name__)

from stateful.views.routes import mod

app.register_blueprint(mod)