from django.utils.text import slugify

from .models import Product, Category, City

class Repo:

    def create_product(self, payload):
        city = City.objects.filter(name=payload.city).first()
        category = Category.objects.filter(name=payload.category).first()

        if city and category:
            new_product = Product.objects.create(
                title = payload.title,
                delivery = payload.delivery,
                is_new = payload.is_new,
                price = payload.price,
                description = payload.description,
                city = city,
                category = category
            )
            new_product.slug = slugify(f'{new_product.title}-{new_product.pk}')

            return new_product.save()