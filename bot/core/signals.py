from django.db.models import signals
from django.dispatch import receiver

from .tasks import create_user_list

from .models import Search

@receiver(signals.post_save ,sender=Search)
def say_hello(sender, instance, created, **kwargs):
    create_user_list.apply_async()
