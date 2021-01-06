from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from .city import City
class Product(models.Model):
    category = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50, verbose_name="Product name")
    slug = models.SlugField(unique=True)
    delivery = models.BooleanField(default=False, verbose_name="True/False")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(
        default=0, verbose_name="Product price")
    description = models.TextField(max_length=3000, null=False, blank=True)
    image = models.ImageField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
