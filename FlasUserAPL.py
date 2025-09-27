from flask import Flask, request, jsonify

app = Flask(_name_)

# In-memory storage
users = {}

@app.route("/")
def home():
    return "User Management API is running!"

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET single user by id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

# POST - create new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error":"name and email required"}), 400
    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"], "email": data["email"]}
    return jsonify(users[user_id]), 201

# PUT - update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json or {}
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

# DELETE - remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify(deleted), 200

if _name_ == "_main_":
    app.run(debug=True)