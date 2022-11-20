"""Flask app factory module."""

from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from ..config import Config


# Make scheduler and SQLAlchemy objects available globally
db = SQLAlchemy()
scheduler = APScheduler()


def create_app(config=Config):
    """Flask app factory."""

    app = Flask(__name__)
    app.config.from_object(config)

    # Initialize plugins
    db.init_app(app)
    db.app = app
    api = Api(app)
    scheduler.init_app(app)
    scheduler.start()
    CORS(app)

    # Add REST endpoints, OpenAPI specs, interfaces
    with app.app_context():

        # Generate marshmallow schemas of db models and create
        from .utils.marshmallow import setup_schema

        setup_schema(db)

        # Initialize resources and generate OpenAPI specs
        from .utils.specs import add_specs
        from .resources import add_resources

        add_resources(api)
        add_specs()

        # Initialize interfaces
        from . import interfaces

    return app
