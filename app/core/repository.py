from django.utils.text import slugify
from django.contrib.auth import get_user_model

from .models import Product, Category, City

User = get_user_model()


class Repo:

    def create_product(self, payload):
        city = City.objects.filter(name=payload.city).first()
        category = Category.objects.filter(name=payload.category).first()
        user = User.objects.filter(email=payload.user_email).first()

        if Product.objects.all():
            last_id = Product.objects.all().last().id
        else:
            last_id = 0

        if city and category and user:
            new_product = Product.objects.create(
                title=payload.title,
                delivery=payload.delivery,
                is_new=payload.is_new,
                price=payload.price,
                description=payload.description,
                city=city,
                category=category,
                user=user,
                slug=slugify(f'{payload.title}-{last_id+1}')
            )
            return new_product

    def update_user_info(self, payload, user):
        user = User.objects.filter(id=user.id).first()
        print(payload.name)
        if user:
            user.name=payload.name,
            user.surname=payload.surname,
            user.email=payload.email,
            user.phone_number=payload.phone_number,

            return user.save()
