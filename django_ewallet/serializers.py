from rest_framework import serializers

from django_ewallet.models import Wallet, Transaction




class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance', 'wallet_number']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['status', 'type', 'date_time', 'amount', 'wallet', 'reference_number']


class CreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type', 'status', 'amount', 'wallet']


