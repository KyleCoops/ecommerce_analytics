from faker import Faker
import random
from app.models.sale import Sale

faker = Faker()

def generate_sales(n=10):
    return [
        Sale(
            sale_id=faker.uuid4(),
            product=faker.word(),
            amount=round(random.uniform(5.0, 200.0), 2),
            timestamp=faker.date_time_this_year().isoformat()
        )
        for _ in range(n)
    ]
