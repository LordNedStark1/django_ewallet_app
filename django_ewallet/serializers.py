from rest_framework import serializers

from django_ewallet.models import Wallet, Transaction


class TransactionActivitySerializer(serializers.Serializer):
    Transaction_Type = [
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
        ('TRANSFER', 'Transfer'),
    ]

    wallet_number = serializers.CharField(max_length=10, required=False)
    transaction_type = serializers.ChoiceField(choices=Transaction_Type, default="Debit")
    amount = serializers.DecimalField(max_digits=9, decimal_places=2)
    description = serializers.CharField(max_length=200, required=False)
    def validate(self, data):
        if data.get('Transaction_Type') == 'DEBIT' and data.get('wallet_number') is None:
            raise serializers.ValidationError(
                "Wallet number must be provided for TRANSFER transactions"
            )
        return super().validate(data)

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


