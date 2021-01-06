from django.contrib import admin

from core.models import Category, City, ProductImage, Product


admin.site.register(City)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Product)
