from flask import Flask

app = Flask(__name__)

from stateful.views import routes, error
app.register_blueprint(routes.page)
app.register_blueprint(error.page)
