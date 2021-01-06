from django.db import models
from core.models import Product


class ProductImage(models.Model):
    name = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
