from stories import story, arguments, Success, Failure, Result

from core.entities import ProductEntity
from core.repository import Repo


class CreateProduct:

    @story
    @arguments(
        'title', 'delivery', 'is_new',
            'price', 'description',
        'city', 'category', 'image', 'email',
    )
    def create(I):

        I.validate_inputs
        I.build_product
        I.persist_product
        I.done

    def validate_inputs(self, ctx):
        if ctx.delivery == 'True':
            ctx.delivery_bool_value = True
        else:
            ctx.delivery_bool_value = False

        if ctx.is_new == 'True':
            ctx.is_new_bool_value = True
        else:
            ctx.is_new_bool_value = False

        return Success()

    def build_product(self, ctx):
        ctx.entity = ProductEntity(
            title=ctx.title,
            delivery=ctx.delivery_bool_value,
            is_new=ctx.is_new_bool_value,
            price=ctx.price,
            description=ctx.description,
            city=ctx.city,
            category=ctx.category,
            image=ctx.image,
            user_email=ctx.email
        )
        return Success()

    def persist_product(self, ctx):
        ctx.result = Repo().create_product(
            payload=ctx.entity
        )
        print(ctx.result)
        return Success()

    def done(self, ctx):
        return Result(ctx.result)
