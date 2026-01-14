# from flask import Blueprint, request, jsonify
# from app.DatabaseMigration import db
# from app.models import User, Book, Library
# from datetime import datetime

# users_bp = Blueprint('users', __name__)

# # status = {
# #     "OK": 200,
# #     "Create": 201,
# #     "NotFound": 404,
# # }


# # =======================================/ Book \=======================================
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GET ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @users_bp.route("/users", methods=["GET"])
# def get_users():
#     users= db.session.execute(db.select(User)).scalars().all()

#     output = [{
#         "ID":     user.id, 
#         "Name":    user.name,
#         "Library": user.library_id,
#         } for user in users]    
    
#     return jsonify(output), 201

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ POST ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @users_bp.route("/users", methods=["POST"])
# def add_user():
#     data = request.get_json()
#     lib_id = data.get("library_id")
#     library = db.session.get(Library, lib_id)
#     if not library: return jsonify({"message": "Bad Request"}), 404
#     newUser = User(
#                    name=data.get("name"),
#                    library_id=lib_id,
#                    )

#     db.session.add(newUser)
#     db.session.commit()

#     return jsonify({"message": "Success!, new User was created", "id": newUser.id}), 201

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @users_bp.route("/users/<int:id>", methods=["PUT"])
# def update_user(id):
#     user = db.session.get(User, id)
#     if not user:
#             return jsonify({"message": "Bad Request"}), 404
#     data = request.get_json()

#     user.name = data.get("title",user.name)
#     user.library_id = data.get("library_id",user.library_id)

#     db.session.commit()

#     return jsonify({"message": f"User {id} updated successfully"})

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DELETE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @users_bp.route("/users/<int:id>", methods=["DELETE"])
# def delete_user(id):
#     user = db.session.get(User, id)
#     if not user:
#             return jsonify({"message": "Bad Request"}), 404

#     db.session.delete(user)
#     db.session.commit()

#     return jsonify({"message": f"Book {id} deleted successfully"})
# # =======================================\ Book /=======================================

# # =======================================/ ADDITIONAL \=======================================
# @users_bp.route("/users/<name>/books", methods=["GET"])
# def get_book(name):
#      user = db.session.execute(db.select(User).where(User.name == name)).scalar_one_or_none()

#      if not user:
#           return jsonify({"message": "Bad Request"}), 404

#      books_list = user.library.books if user.library else []
          
#      return jsonify({"user": name, "book_count": len(books_list), "books": [book.title for book in books_list]}), 200


     

# # =======================================\ ADDITIONAL /=======================================

from flask import Blueprint
from app.controllers import user_controller as controller

users_bp = Blueprint('users', __name__)

@users_bp.route("/users", methods=["GET"])
def get_users():
    return controller.get_users_logic()

@users_bp.route("/users", methods=["POST"])
def add_user():
    return controller.add_user_logic()

@users_bp.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    return controller.update_user_logic(id)

@users_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    return controller.delete_user_logic(id)

@users_bp.route("/users/<name>/books", methods=["GET"])
def get_user_books(name):
    return controller.get_user_books_logic(name)