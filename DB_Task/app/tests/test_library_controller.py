import pytest
from app import create_app
from app.controllers import library_controller as lc
from app.utils.constants import STATUS as status

@pytest.fixture
def app():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    with app.app_context():
        from app.DatabaseMigration import db
        db.create_all()
        yield app

def test_add_library(app):
    with app.test_request_context(json={"name": "Central Library"}):
        res, code = lc.add_library_logic()
        assert code == status["Create"]

def test_get_libraries(app):
    with app.test_request_context():
        res, code = lc.get_libraries_logic()
        assert code == status["OK"]

def test_delete_library(app):
    with app.test_request_context():
        res, code = lc.delete_library_logic(1) # ID 1 likely won't exist in memory
        assert code in [status["OK"], status["NotFound"]]

def test_update_library(app):
    with app.test_request_context(json={"name": "New Name"}):
        res, code = lc.update_library_logic(1)
        assert code in [status["OK"], status["NotFound"]]

def test_get_library_books(app):
    with app.test_request_context():
        res, code = lc.get_library_books_logic(1)
        assert code in [status["OK"], status["NotFound"]]