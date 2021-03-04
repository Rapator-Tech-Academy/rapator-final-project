from dataclasses import dataclass

from PIL import Image
    
@dataclass
class ProductEntity:
    title: str
    delivery: bool
    is_new: bool
    price: float
    description: str
    city: str
    category: str
    image: Image
    user_email: str