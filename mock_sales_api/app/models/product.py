from dataclasses import dataclass, asdict

@dataclass
class Product:
    product_id: str
    name: str
    category: str
    price: float

    def dict(self):
        return asdict(self)
