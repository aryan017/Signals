from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Car
from buyers.models import Buyer

@receiver(post_save,sender=Car)
def post_save_create_buyer(sender,instance,created,**kwargs):
    print('sender',sender)
    print('instance',instance)
    print('created',created)
    if created:
        Buyer.objects.create(name=instance)