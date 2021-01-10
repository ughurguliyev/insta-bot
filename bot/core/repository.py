from .models import Search, File

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
        return new_search
    
    def write_file(self, data, title):
        splitted_title = title.lower().split()
        file_title = '-'.join(splitted_title)

        with open(f'media/users/files/{file_title}.txt', mode='w') as file:
            for i in data:
                file.write(f'{i} \n')

        queryset = Search.objects.filter(title=title).first()

        new_file = File.objects.create(
            default_user_img = f'users/files/{file_title}.txt'
        )

        queryset.default_img_file = new_file
        queryset.is_finished = True
        queryset.save()

        

