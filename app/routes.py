from flask import Blueprint, jsonify, request
from app.auth import verify_credentials

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    return jsonify({"status": "running", "service": "DevSecOps Demo API"}), 200

@main_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    
    if verify_credentials(username, password):
        return jsonify({"message": f"Welcome {username}!"}), 200
    return jsonify({"error": "Invalid credentials"}), 401