from stories import story, arguments, Success, Failure, Result

from core.repository import Repo

class EditProduct:

    @story
    @arguments('product', 'title', 'price', 'description')
    def update(I):
        I.validate_inputs
        I.persist_product
        I.done
    
    def validate_inputs(self, ctx):
        return Success()
    
    def persist_product(self, ctx):
        ctx.result = Repo().update_product(
            product = ctx.product,
            title = ctx.title, 
            price = ctx.price, 
            description = ctx.description,
        )
        return Success()
    
    def done(self, ctx):
        return Result(ctx.result)
    
