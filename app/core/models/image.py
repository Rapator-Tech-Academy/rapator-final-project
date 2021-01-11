from django.db import models
from core.models import Product


class ProductImage(models.Model):
    name = models.ManyToManyField(Product, default=None)
    image = models.ImageField(upload_to="images/")
