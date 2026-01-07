from flask import Flask
from app.DatabaseMigration import db, migrate

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

    db.init_app(app)
    migrate.init_app(app, db)

    # We register the routes here
    from app.routes import app_bp
    app.register_blueprint(app_bp)

    return app