from rest_framework import serializers

from request.models import PaymentRequest, Requisite


class RequisiteReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisite
        fields = '__all__'


class PaymentRequestReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = '__all__'
