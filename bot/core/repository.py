from django.db.models.deletion import SET_NULL
from .models import Search

class Repo:
    def create_search(self, payload):
        new_search = Search(
            username = payload.username,
            title = payload.title,
            note = payload.note,
        )
        if Search.objects.filter(title__icontains=new_search.title):
            length = len(Search.objects.filter(title__icontains=new_search.title))
            new_search.title = f'{payload.title} v.{length+1}'

        new_search.save()
    
    def write_file(self, data):
        with open('media/users/files/users.txt', mode='w') as file:
            for i in data:
                file.write(f'{i} \n')