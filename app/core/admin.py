from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from mptt.admin import MPTTModelAdmin
from ckeditor.widgets import CKEditorWidget
from mptt.admin import MPTTModelAdmin

from core.models import Category, City, ProductImage, Product


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }




admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

admin.site.register(City)
admin.site.register(Category, MPTTModelAdmin)

admin.site.register(ProductImage)
admin.site.register(Product)

