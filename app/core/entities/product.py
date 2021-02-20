from dataclasses import dataclass
    
@dataclass
class ProductEntity:
    title: str
    delivery: bool
    is_new: bool
    price: float
    description: str
    city: str
    category: str
    user_email: str