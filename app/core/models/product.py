from django.db import models
from django.utils.text import slugify

from .category import Category
from app.utils.helpers import STATUS_TYPES
from .city import City


class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Product name")
    slug = models.SlugField(unique=True)
    delivery = models.BooleanField(default=False, verbose_name="Çatdırılma")
    is_new = models.BooleanField(default=True, verbose_name="Yeni?")
    status = models.IntegerField(choices=STATUS_TYPES, default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(
        default=0, verbose_name="Product price")
    description = models.TextField(max_length=3000, null=False, blank=True)
    image = models.ImageField(blank=True)
    view_count=models.PositiveIntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return self.slug
 
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
