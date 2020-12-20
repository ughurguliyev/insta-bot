from django.db import models
from treebeard.mp_tree import MP_Node

# Create your models here.


class File(models.Model):
    default_user_img = models.FileField(verbose_name='Users using default image', upload_to='users/files')

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
    
    def __str__(self):
        return f'Search - {self.pk}'


class Search(models.Model):
    title = models.CharField(max_length=400, unique=True, verbose_name='Search title')
    default_img_file = models.ForeignKey(File, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=200, verbose_name='Username', null=True)
    note = models.TextField(verbose_name='Note', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Search'
        verbose_name_plural = 'Searches'
    
    def __str__(self):
        return self.title
    
