from flask import request, jsonify
from app.DatabaseMigration import db
from app.models import Library
from app.utils.constants import STATUS as status

def add_library_logic():
    data = request.get_json()
    newLibrary = Library(name=data.get("name"))
    db.session.add(newLibrary)
    db.session.commit()
    return jsonify({"message": "Success!, new library was created", "id": newLibrary.id}), status["Create"]

def get_libraries_logic():
    libraries = db.session.execute(db.select(Library)).scalars().all()
    output = [{"id": library.id, "Name": library.name} for library in libraries]
    return jsonify(output), status["OK"]

def delete_library_logic(id):
    library = db.session.get(Library, id)
    if not library:
        return jsonify({"message": "Failed!, library not found"}), status["NotFound"]
    db.session.delete(library)
    db.session.commit()
    return jsonify({"message": f"Library {id} deleted successfully"}), status["OK"]

def update_library_logic(id):
    library = db.session.get(Library, id)
    if not library:
        return jsonify({"message": "Failed!, library not found"}), status["NotFound"]
    data = request.get_json()
    library.name = data.get("name", library.name)
    db.session.commit()
    return jsonify({"message": f"Library {id} updated successfully"}), status["OK"]

def get_library_books_logic(id):
    library = db.session.get(Library, id)
    if not library:
        return jsonify({"message": "Library not found"}), status["NotFound"]
    books = [{"id": b.id, "title": b.title} for b in library.books]
    return jsonify({"library": library.name, "books": books}), status["OK"]