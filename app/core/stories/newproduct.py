from stories import story, arguments, Success, Failure, Result

from core.entities import ProductEntity
from core.repository import Repo

class CreateProduct:

    @story
    @arguments('title', 'delivery', 'is_new', 'price', 'description', 'city', 'category')
    def create(I):

        I.validate_inputs
        I.build_product
        I.persist_product
        I.done 
    
    def validate_inputs(self, ctx):
        return Success()

    def build_product(self, ctx):
        ctx.entity = ProductEntity(
            title = ctx.title,
            delivery = ctx.delivery,
            is_new = ctx.is_new,
            price = ctx.price,
            description = ctx.description,
            city = ctx.city,
            category = ctx.category,
        )
        return Success()
    
    def persist_product(self, ctx):
        print(ctx.entity.title)
        ctx.result = Repo().create_product(
            payload = ctx.entity
        )
        return Success()
    
    def done(self, ctx):
        return Result(ctx.result)