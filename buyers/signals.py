from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User # sender
from .models import Buyer  # receiver

@receiver(post_save,sender=User) #@receiver is a decorator
def post_save_create_buyer(sender,instance,created,**kwargs):
    # print('sender',sender)
    # print('instance',instance)
    # print('created',created)
    if created:
        Buyer.objects.create(user=instance)