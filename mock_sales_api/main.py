from flask import Flask
from app.routes.sales import sales_bp
from app.routes.products import products_bp
from app.routes.customers import customers_bp

app = Flask(__name__)

app.register_blueprint(sales_bp)
app.register_blueprint(products_bp)
app.register_blueprint(customers_bp)

@app.errorhandler(400)
def bad_request(e):
    return {"error": "Bad request"}, 400

@app.errorhandler(404)
def not_found(e):
    return {"error": "Not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)