from dataclasses import dataclass, asdict

@dataclass
class Sale:
    sale_id: str
    product: str
    amount: float
    timestamp: str

    def dict(self):
        return asdict(self)
