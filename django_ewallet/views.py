from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from django_ewallet.models import Wallet, Transaction

from django_ewallet.serializers import WalletSerializer, TransactionSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
