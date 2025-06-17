from dataclasses import dataclass, asdict

@dataclass
class Customer:
    customer_id: str
    name: str
    email: str
    join_date: str

    def dict(self):
        return asdict(self)
