from flask import Blueprint, request, jsonify
from app.services.sales_service import generate_sales

sales_bp = Blueprint("sales", __name__, url_prefix="/sales")

@sales_bp.route("/", methods=["GET"])
def get_sales():
    try:
        n = int(request.args.get("n", 10))
        if n < 1 or n > 100:
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid 'n' parameter. Must be 1–100."}), 400

    return jsonify([sale.dict() for sale in generate_sales(n)])
