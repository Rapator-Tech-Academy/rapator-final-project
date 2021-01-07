from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
