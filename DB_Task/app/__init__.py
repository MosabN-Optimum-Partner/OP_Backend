import os
from flask import Flask
from dotenv import load_dotenv
from app.DatabaseMigration import db, migrate

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///project.db")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "private_key")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import all_bp
    for bp in all_bp:
        app.register_blueprint(bp)
    

    return app