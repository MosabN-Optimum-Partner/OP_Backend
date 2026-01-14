import pytest # type: ignore
from app import create_app
from app.controllers import user_controller as uc
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

def test_get_users(app):
    with app.test_request_context():
        res, code = uc.get_users_logic()
        assert code == status["OK"]

def test_add_user(app):
    with app.test_request_context(json={"name": "John Doe", "library_id": 1}):
        res, code = uc.add_user_logic()
        assert code in [status["Create"], status["NotFound"]]

def test_update_user(app):
    with app.test_request_context(json={"name": "Jane Doe"}):
        res, code = uc.update_user_logic(1)
        assert code in [status["OK"], status["NotFound"]]

def test_delete_user(app):
    with app.test_request_context():
        res, code = uc.delete_user_logic(1)
        assert code in [status["OK"], status["NotFound"]]

def test_get_user_books(app):
    with app.test_request_context():
        res, code = uc.get_user_books_logic("John Doe")
        assert code in [status["OK"], status["NotFound"]]