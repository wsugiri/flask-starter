from flask import Blueprint, jsonify
from ..handlers.user import get_users
import os

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["GET"])
def users():
    users = get_users()
    
    return jsonify({
        "cnstring": os.getenv('DB_DATA'),
        "items": users
    })
