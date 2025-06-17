from faker import Faker
from app.models.customer import Customer

faker = Faker()

def generate_customers(n=10):
    return [
        Customer(
            customer_id=faker.uuid4(),
            name=faker.name(),
            email=faker.email(),
            join_date=faker.date_this_decade().isoformat()
        )
        for _ in range(n)
    ]
