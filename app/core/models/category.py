from django.db import models
from django.core.validators import FileExtensionValidator
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    icon = models.FileField(verbose_name='Parent category icon', validators=[FileExtensionValidator(['jpeg', 'jpg', 'svg'])], null=True, blank=True)

    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = "categories"

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return '/'.join(full_path[::-1])
