import pytest # type: ignore
from app import create_app
from app.controllers import book_controller as bc
from app.utils.constants import STATUS

@pytest.fixture
def app():
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    with app.app_context():
        from app.DatabaseMigration import db
        db.create_all()
        yield app


def test_get_books(app):
    with app.test_request_context():
        res, code = bc.get_books_logic()
        assert code == STATUS["OK"]

def test_add_book(app):
    with app.test_request_context(json={"title": "T", "author": "A", "library_id": 1}):
        res, code = bc.add_book_logic()
        assert code in [STATUS["Create"], STATUS["NotFound"]]

def test_update_book(app):
    with app.test_request_context(json={"title": "New"}):
        res, code = bc.update_book_logic(1)
        assert code in [STATUS["OK"], STATUS["BadRequest"]]

def test_delete_book(app):
    with app.test_request_context():
        res, code = bc.delete_book_logic(1)
        assert code in [STATUS["OK"], STATUS["BadRequest"]]

def test_search_books(app):
    with app.test_request_context(query_string={"title": "Harry"}):
        res, code = bc.search_book_logic()
        assert code == STATUS["OK"]

def test_transfer_book(app):
    with app.test_request_context(json={"book_id": 1, "library_id": 2}):
        res, code = bc.transfer_logic()
        assert code in [STATUS["OK"], STATUS["NotFound"]]