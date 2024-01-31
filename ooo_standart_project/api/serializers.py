from rest_framework import serializers

from request.models import PaymentRequest, Requisite


class RequisiteReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisite
        fields = ('payment_type', 'account_type', 'first_name', 'last_name',
                  'middle_name', 'phone_number', 'card_limit', 'created')


class PaymentRequestReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ('amount', 'requisites', 'status', 'created')


class PaymentRequestMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ('status',)
        read_only_fields = ['amount', 'requisites', 'created']


class PaymentRequestWriteSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, write_only=True)

    class Meta:
        model = PaymentRequest
        fields = ('id', 'requisites', 'amount')
        extra_kwargs = {
            'amount': {'write_only': True, 'read_only': True},
        }
