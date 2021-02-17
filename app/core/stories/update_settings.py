from stories import story, arguments, Success, Failure, Result
from django.contrib.auth import get_user_model

from core.entities import UserEntity

User = get_user_model()


class UpdateAccount:

    @story
    @arguments('form')
    def create(I):

        I.validate_inputs
        I.build_entity
        I.persist
        I.done

    def validate_inputs(self, ctx):
        if User.name is None:
            ctx.name = User.name
        else:
            return ctx.name

        return Success()

    def build_entity(self, ctx):
        ctx.entity = UserEntity(
            name=ctx.form.cleaned_data.get('name'),
            surname=ctx.form.cleaned_data.get('surname'),
            email=ctx.form.cleaned_data.get('email'),
            phone_number=ctx.form.cleaned_data.get('phone_number'),
            password=ctx.form.cleaned_data.get('password')
        )
        return Success()

    def persist(self, ctx):
        ctx.result = Repo().update_user_info(
            payload=ctx.entity
        )
        return Success()

    def done(self, ctx):
        return Result(ctx.result)
