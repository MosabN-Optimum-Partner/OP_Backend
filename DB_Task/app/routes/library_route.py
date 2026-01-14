# from app.models import Library
# from flask import Blueprint, request, jsonify
# from app.DatabaseMigration import db

# libraries_bp = Blueprint('libraries', __name__)

# # =======================================/ LIBRARY \=======================================
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @libraries_bp.route("/libraries", methods=["POST"])
# def add_library():
#     data = request.get_json()
#     newLibrary = Library(name=data.get("name"))

#     db.session.add(newLibrary)
#     db.session.commit()

#     return jsonify({"message": "Success!, new library was created", "id": newLibrary.id}), 201

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @libraries_bp.route("/libraries", methods=["GET"])
# def get_libraries():
#     libraries= db.session.execute(db.select(Library)).scalars().all()

#     output = []    
#     for library in libraries:
#         output.append({"id":library.id, "Name": library.name})
#     return jsonify(output), 200

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DELETE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @libraries_bp.route("/libraries/<int:id>", methods=["DELETE"])
# def delete_library(id):
#     library = db.session.get(Library, id)
#     if not library:
#             return jsonify({"message": "Faild!, library not found"}), 404

#     db.session.delete(library)
#     db.session.commit()

#     return jsonify({"message": f"Library {id} deleted successfully"})

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @libraries_bp.route("/libraries/<int:id>", methods=["PUT"])
# def update_library(id):
#     library = db.session.get(Library, id)
#     if not library:
#             return jsonify({"message": "Faild!, library not found"}), 404
#     data = request.get_json()

#     library.name = data.get("name",library.name)
#     db.session.commit()

#     return jsonify({"message": f"Library {id} updated successfully"})
# # =======================================\ LIBRARY /=======================================

# # =======================================/ ADDITIONAL \=======================================
# @libraries_bp.route("/libraries/<int:id>/books", methods=["GET"])
# def get_library_books(id):
#     library = db.session.get(Library, id)
#     if not library:
#         return jsonify({"message": "Library not found"}), 404
    
#     books = [{"id": b.id, "title": b.title} for b in library.books]
#     return jsonify({"library": library.name, "books": books}), 200
# # =======================================\ ADDITIONAL /=======================================


from flask import Blueprint
from app.controllers import library_controller as controller

libraries_bp = Blueprint('libraries', __name__)

@libraries_bp.route("/libraries", methods=["POST"])
def add_library():
    return controller.add_library_logic()

@libraries_bp.route("/libraries", methods=["GET"])
def get_libraries():
    return controller.get_libraries_logic()

@libraries_bp.route("/libraries/<int:id>", methods=["DELETE"])
def delete_library(id):
    return controller.delete_library_logic(id)

@libraries_bp.route("/libraries/<int:id>", methods=["PUT"])
def update_library(id):
    return controller.update_library_logic(id)

@libraries_bp.route("/libraries/<int:id>/books", methods=["GET"])
def get_library_books(id):
    return controller.get_library_books_logic(id)