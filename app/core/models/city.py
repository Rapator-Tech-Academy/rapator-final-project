from django.db import models

from autoslug import AutoSlugField

class City(models.Model):
    name = models.CharField(max_length=35)
    slug = AutoSlugField(populate_from='name')


    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
    
    def __str__(self):
        return self.name