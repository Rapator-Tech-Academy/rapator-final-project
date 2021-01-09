from stories import story, arguments, Success, Failure, Result

from core.entities import ProductEntity
from core.repository import Repo

class CreateProduct:

    @story
    @arguments('form')
    def create(I):

        I.validate_inputs
        I.build_product
        I.persist_product
        I.done 
    
    def validate_inputs(self, ctx):
        if ctx.form.data.get('delivery') == None:
            ctx.delivery = False
        else:
            ctx.delivery = True

        if ctx.form.data.get('is_new') == None:
            ctx.is_new = False
        else:
            ctx.is_new = True 

        return Success()

    def build_product(self, ctx):
        ctx.entity = ProductEntity(
            title = ctx.form.cleaned_data.get('title'),
            delivery = ctx.delivery,
            is_new = ctx.is_new,
            price = ctx.form.cleaned_data.get('price'),
            description = ctx.form.cleaned_data.get('description'),
            city = ctx.form.cleaned_data.get('city'),
            category = ctx.form.cleaned_data.get('category'),
            user_email = ctx.form.cleaned_data.get('email')
        )
        return Success()
    
    def persist_product(self, ctx):
        ctx.result = Repo().create_product(
            payload = ctx.entity
        )
        print(ctx.result)
        return Success()
    
    def done(self, ctx):
        return Result(ctx.result)