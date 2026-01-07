from flask import Blueprint, request, jsonify
from app.DatabaseMigration import db
from app.models import Library, Book
from datetime import datetime

app_bp = Blueprint('main', __name__)


# =======================================/ LIBRARY \=======================================

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app_bp.route("/libraries", methods=["POST"])
def add_library():
    data = request.get_json()
    newLibrary = Library(name=data.get("name"))

    db.session.add(newLibrary)
    db.session.commit()

    return jsonify({"message": "Success!, new library was created", "id": newLibrary.id}), 201

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app_bp.route("/libraries", methods=["GET"])
def get_libraries():
    libraries= db.session.execute(db.select(Library)).scalars().all()

    output = []    
    for library in libraries:
        output.append({"id":library.id, "Name": library.name})
    return jsonify(output), 200

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app_bp.route("/libraries/<int:id>", methods=["DELETE"])
def delete_library(id):
    library = db.session.get(Library, id)
    if not library:
            return jsonify({"message": "Faild!, library not found"}), 404

    db.session.delete(library)
    db.session.commit()

    return jsonify({"message": f"Library {id} deleted successfully"})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DELETE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app_bp.route("/libraries/<int:id>", methods=["PUT"])
def update_library(id):
    library = db.session.get(Library, id)
    if not library:
            return jsonify({"message": "Faild!, library not found"}), 404
    data = request.get_json()

    library.name = data.get("name",library.name)
    db.session.commit()

    return jsonify({"message": f"Library {id} updated successfully"})

# =======================================\ LIBRARY /=======================================


# =======================================/ Book \=======================================


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app_bp.route("/books", methods=["GET"])
def get_books():
    books= db.session.execute(db.select(Book)).scalars().all()

    output = []    
    for book in books:
        output.append({"ID":book.id, 
                       "Title": book.title, 
                       "Author": book.author, 
                       "Library ID": book.library_id, 
                       "Created At": book.created_at,})
    return jsonify(output), 200

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app_bp.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    newBook = Book(title=data.get("title"),author=data.get("author"),library_id=data.get("library_id"),created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    db.session.add(newBook)
    db.session.commit()

    return jsonify({"message": "Success!, new Book was created", "id": newBook.id}), 201

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@app_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = db.session.get(Book, id)
    if not book:
            return jsonify({"message": "Faild!, book not found"}), 404
    data = request.get_json()

    book.title = data.get("title",book.title)
    book.author = data.get("author",book.author)
    book.library_id = data.get("library_id",book.library_id)
    book.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db.session.commit()

    return jsonify({"message": f"Book {id} updated successfully"})

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DELETE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
@app_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = db.session.get(Book, id)
    if not book:
            return jsonify({"message": "Faild!, book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": f"Book {id} deleted successfully"})


# =======================================\ Book /=======================================


# =======================================/ ADDITIONAL \=======================================

@app_bp.route("/books/search", methods=["GET"])
def search_book():
     term = request.args.get("term", "")
     query = db.select(Book).where(
        (Book.title.ilike(f"%{term}%")) | (Book.author.ilike(f"%{term}%")))
     results = db.session.execute(query).scalars().all()
     return jsonify([{"title": b.title, "author": b.author} for b in results]), 200

@app_bp.route("/libraries/<int:id>/books", methods=["GET"])
def get_library_books(id):
    library = db.session.get(Library, id)
    if not library:
        return jsonify({"message": "Library not found"}), 404
    
    books = [{"id": b.id, "title": b.title} for b in library.books]
    return jsonify({"library": library.name, "books": books}), 200


# =======================================\ ADDITIONAL /=======================================
