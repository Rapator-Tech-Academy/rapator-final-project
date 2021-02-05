from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from mptt.admin import MPTTModelAdmin
from ckeditor.widgets import CKEditorWidget
from mptt.admin import MPTTModelAdmin

from core.models import Category, City, ProductImage, Product, ActiveUserDetail


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class ActiveUserAdmin(admin.ModelAdmin): #added
    list_display =['ip','is_user', 'visited_time',]


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

admin.site.register(City)
admin.site.register(Category, MPTTModelAdmin)

admin.site.register(ProductImage)
admin.site.register(Product)

admin.site.register(ActiveUserDetail, ActiveUserAdmin) #added
