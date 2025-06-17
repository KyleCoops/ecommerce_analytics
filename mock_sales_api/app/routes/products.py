from flask import Blueprint, request, jsonify
from app.services.product_service import generate_products

products_bp = Blueprint("products", __name__, url_prefix="/products")

@products_bp.route("/", methods=["GET"])
def get_products():
    try:
        n = int(request.args.get("n", 10))
        if n < 1 or n > 50:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid 'n' parameter. Must be 1–50."}), 400

    return jsonify([p.dict() for p in generate_products(n)])
