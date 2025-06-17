from faker import Faker
from app.models.product import Product

faker = Faker()

def generate_products(n=10):
    return [
        Product(
            product_id=faker.uuid4(),
            name=faker.word(),
            category=faker.random_element(elements=["electronics", "books", "clothing"]),
            price=round(faker.random_number(digits=4) / 100.0, 2)
        )
        for _ in range(n)
    ]
