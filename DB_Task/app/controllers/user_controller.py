from flask import request, jsonify
from app.DatabaseMigration import db
from app.models import User, Library
from app.utils.constants import STATUS as status

def get_users_logic():
    users = db.session.execute(db.select(User)).scalars().all()
    output = [{
        "ID": user.id, 
        "Name": user.name,
        "Library": user.library_id,
    } for user in users]    
    return jsonify(output), status["OK"] # Changed from 201 to OK (200) for a GET

def add_user_logic():
    data = request.get_json()
    lib_id = data.get("library_id")
    library = db.session.get(Library, lib_id)
    if not library: 
        return jsonify({"message": "Bad Request"}), status["NotFound"]
    
    newUser = User(
        name=data.get("name"),
        library_id=lib_id,
    )
    db.session.add(newUser)
    db.session.commit()
    return jsonify({"message": "Success!, new User was created", "id": newUser.id}), status["Create"]

def update_user_logic(id):
    user = db.session.get(User, id)
    if not user:
        return jsonify({"message": "Bad Request"}), status["NotFound"]
    data = request.get_json()

    # Fixed: your code had data.get("title") for user name, kept it but logic is user.name
    user.name = data.get("name", user.name) 
    user.library_id = data.get("library_id", user.library_id)

    db.session.commit()
    return jsonify({"message": f"User {id} updated successfully"}), status["OK"]

def delete_user_logic(id):
    user = db.session.get(User, id)
    if not user:
        return jsonify({"message": "Bad Request"}), status["NotFound"]

    db.session.delete(user)
    db.session.commit()
    # Fixed typo: changed "Book" to "User" to match the route
    return jsonify({"message": f"User {id} deleted successfully"}), status["OK"]

def get_user_books_logic(name):
    user = db.session.execute(db.select(User).where(User.name == name)).scalar_one_or_none()
    if not user:
        return jsonify({"message": "Bad Request"}), status["NotFound"]

    books_list = user.library.books if user.library else []
    return jsonify({
        "user": name, 
        "book_count": len(books_list), 
        "books": [book.title for book in books_list]
    }), status["OK"]