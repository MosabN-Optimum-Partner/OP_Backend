# from flask import Blueprint, request, jsonify
# from app.DatabaseMigration import db
# from app.models import Book, Library
# from datetime import datetime

# books_bp = Blueprint('books', __name__)

# status = {
#     "OK": 200,
#     "Create": 201,
#     "NotFound": 404,
#     "BadRequest": 400,
# }


# # =======================================/ Book \=======================================
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @books_bp.route("/books", methods=["GET"])
# def get_books():
#     books= db.session.execute(db.select(Book)).scalars().all()

#     output = [ {"ID":book.id, 
#                        "Title": book.title, 
#                        "Author": book.author, 
#                        "Library ID": book.library_id, 
#                        "Created At": book.created_at,} for book in books]
    
#     return jsonify(output), status.get("OK")

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @books_bp.route("/books", methods=["POST"])
# def add_book():
#     data = request.get_json()
#     book_title = data.get("title")
#     book_author = data.get("author")
#     library_id = data.get("library_id")
#     if (not book_title or not book_author or not library_id):
#          return jsonify({"message": "Bad Request"}), status["BadRequest"]
    
#     library = db.session.get(Library, library_id)
#     if (not library):
#          return jsonify({"message": "Library not found"}), status["NotFound"]
    

#     newBook = Book(title=book_title,
#                    author=book_author,
#                    library_id=library_id,
#                    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                    )

#     db.session.add(newBook)
#     db.session.commit()

#     return jsonify({"message": "Success!, new Book was created", "id": newBook.id}), status.get("Create")

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @books_bp.route("/books/<int:id>", methods=["PUT"])
# def update_book(id):
#     book = db.session.get(Book, id)
#     if not book:
#             return jsonify({"message": "Failed!, book not found"}), status["BadRequest"]
#     data = request.get_json()

#     book.title = data.get("title",book.title)
#     book.author = data.get("author",book.author)
#     book.library_id = data.get("library_id",book.library_id)
#     book.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     db.session.commit()

#     return jsonify({"message": f"Book {id} updated successfully"})

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DELETE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @books_bp.route("/books/<int:id>", methods=["DELETE"])
# def delete_book(id):
#     book = db.session.get(Book, id)
#     if not book:
#             return jsonify({"message": "Failed!, book not found"}), status["BadRequest"]

#     db.session.delete(book)
#     db.session.commit()

#     return jsonify({"message": f"Book {id} deleted successfully"})
# # =======================================\ Book /=======================================

# # =======================================/ ADDITIONAL \=======================================
# @books_bp.route("/books/search", methods=["GET"])
# def search_book():
#      title = request.args.get("title", "")
#      author = request.args.get("author", "")
#      query = db.select(Book)
#      if title:
#         query = query.where(Book.title.ilike(f"%{title}%"))
#      if author:
#         query = query.where(Book.author.ilike(f"%{author}%"))

#      results = db.session.execute(query).scalars().all()
     
#      output = [{"title": b.title, "author": b.author} for b in results]
#      return jsonify(output), status["OK"]

# @books_bp.route("/books/transfer", methods=["POST"])
# def transfer():
#      data = request.get_json()
#      book_id = data.get("book_id")
#      new_library_id = data.get("library_id")

#      if not book_id and not new_library_id:
#         return jsonify({"message": "Bad Request"}), status["BadRequest"]
#      book = db.session.get(Book, book_id)
#      to_library = db.session.get(Library, new_library_id)

#      if(not book or not to_library):
#         return jsonify({"message": "Not Found"}), status["NotFound"]

#      old_lib_id = book.library_id
#      book.library_id = new_library_id
#      db.session.commit()
#      return jsonify({"message": "Transfer successful",
#                      "Book": book.title,
#                      "from_library": old_lib_id,
#                      "to_library": new_library_id}) , status["OK"]


# # =======================================\ ADDITIONAL /=======================================





from flask import Blueprint
from app.controllers import book_controller as controller

books_bp = Blueprint('books', __name__)

@books_bp.route("/books", methods=["GET"])
def get_books():
    return controller.get_books_logic()

@books_bp.route("/books", methods=["POST"])
def add_book():
    return controller.add_book_logic()

@books_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    return controller.update_book_logic(id)

@books_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    return controller.delete_book_logic(id)

@books_bp.route("/books/search", methods=["GET"])
def search_book():
    return controller.search_book_logic()

@books_bp.route("/books/transfer", methods=["POST"])
def transfer():
    return controller.transfer_logic()