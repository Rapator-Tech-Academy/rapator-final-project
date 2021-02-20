from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from app.utils.helpers import STATUS_TYPES
from django.utils.text import slugify

from .city import City
from .category import Category
from .image import ProductImage

User = get_user_model()

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
    image = models.ImageField(blank=True, null=True, default='images/demo.png')

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='category')
    view_count = models.PositiveIntegerField(default=0)
    daily_view_count = models.PositiveIntegerField(default=0)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return self.slug
 
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug

    def get_image_url(self):
        return self.image.url
    
    @property
    def is_past_due(self):
        keyword = ""

        if self.updated_at == timezone.now():
            keyword = 'bugün'
        else:
            keyword = self.updated_at.strftime("%d.%m.%Y")

        return keyword
    
    @property
    def product_id(self):
        return 1000 + self.pk

    def save(self, **kwargs):
        if not self.slug:
            slug = f"{self.title[:5]}"
            self.slug = slugify(slug)
            return super().save(**kwargs)

        return super(Product, self).save(**kwargs)

    
