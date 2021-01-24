from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from .category import Category
from app.utils.helpers import STATUS_TYPES
from django.utils.text import slugify

from .city import City

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=50, verbose_name="Product name")
    slug = models.SlugField(unique=True, null=True, blank=True)
    delivery = models.BooleanField(default=False, verbose_name="Çatdırılma")
    is_new = models.BooleanField(default=True, verbose_name="Yeni?")
    status = models.IntegerField(choices=STATUS_TYPES, default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, verbose_name="Product price")
    description = models.TextField(max_length=3000, null=False, blank=True)
    image = models.ImageField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    view_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    def get_image_url(self):
        return self.image.url

    def save(self, **kwargs):
        if not self.slug:
            slug = f"{self.title[:5]}"
            self.slug = slugify(slug)
            return super().save(**kwargs)
        return super().save(**kwargs)
