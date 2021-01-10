from stories import story, arguments, Success, Failure, Result

from .entities import SearchEntity
from .repository import Repo
from .tasks import create_user_list

class CreateSearch:

    @story
    @arguments('username', 'search_title', 'note')
    def create(I):
        I.validate_input
        I.create_entity
        I.load_data
        I.add_task
        I.done
    
    def validate_input(self, ctx):
        return Success()
    
    def create_entity(self, ctx):
        ctx.entity = SearchEntity(
            username = ctx.username,
            title = ctx.search_title,
            note = ctx.note
        )
        return Success()
    
    def load_data(self, ctx):
        ctx.result = Repo().create_search(
            payload = ctx.entity
        )
        return Success()
    
    def add_task(self, ctx):
        create_user_list.delay(instance=ctx.result.title)
        return Success()
    
    def done(self, ctx):
        return Result(ctx.result)