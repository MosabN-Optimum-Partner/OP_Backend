from .book_route import books_bp
from .library_route import libraries_bp
from .user_route import users_bp


all_bp = [books_bp, libraries_bp, users_bp]