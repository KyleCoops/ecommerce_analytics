from flask import Blueprint, request, jsonify
from app.services.customer_service import generate_customers

customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("/", methods=["GET"])
def get_customers():
    try:
        n = int(request.args.get("n", 10))
        if n < 1 or n > 50:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid 'n' parameter. Must be 1–50."}), 400

    return jsonify([c.dict() for c in generate_customers(n)])
