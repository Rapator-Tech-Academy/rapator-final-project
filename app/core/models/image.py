from django.db import models

class ProductImage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    image = models.ImageField(upload_to="images/")
