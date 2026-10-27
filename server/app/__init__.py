import os

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from app.config import settings
from app.extensions import api, db, migrate
from app.resources import init_namespaces


def create_app(config_name: str = os.getenv("FLASK_CONFIG") or "development") -> Flask:
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(settings[config_name])

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    api.init_app(app)

    from app.models import User

    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "user": User}

    init_namespaces(api)

    return app
