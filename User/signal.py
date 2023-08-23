from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from User.models import User
from django_ewallet.models import Wallet

@receiver(post_save, sender = User)
def create_wallet (sender,instance,created,**kwargs):
    if created:
        Wallet.objects.create(
            user = instance, wallet_number= instance.phone[1:]
        )