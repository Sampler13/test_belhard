from flask import Flask
from database.model import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object('config.Config')
    app.secret_key = 'asdsadasd asdsadsad asdasdasd'
    db.init_app(app)


    from . import routes
    app.register_blueprint(routes.bp)
    return app