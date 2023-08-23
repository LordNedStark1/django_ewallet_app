import uuid

from django.db import models

from AppBuild import settings


class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    accountNumber = models.CharField(max_length=10, primary_key=True)
    balance = models.DecimalField(decimal_places=2,max_digits=9)


class Transaction(models.Model):
    TYPE = [
        ('DEPOSIT', 'deposit'),
        ('WITHDRAW', 'withdraw'),
        ('TRANSFER', 'transfer')
    ]
    STATUS = [
        ('PENDING', 'pending'),
        ('SUCCESS', 'success'),
        ('DECLINED', 'declined')
    ]
    date_time = models.DateField(blank=True, null=True)
    reference_number = models.UUIDField( primary_key = True,default = uuid.uuid4,editable = False)
    wallet = models.ManyToOneRel(Wallet, on_delete=models.CASCADE, to=Wallet, field_name='Wallet')
