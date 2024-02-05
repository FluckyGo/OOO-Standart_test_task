from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth import get_user_model


from .serializers import (PaymentRequestReadSerializer,
                          RequisiteReadSerializer,
                          PaymentRequestMiniSerializer,
                          PaymentRequestWriteSerializer)
from request.models import Requisite, PaymentRequest
from .pagination import RequestPagination
from .mixins import BaseViewSet


User = get_user_model()


class RequisiteViewSet(BaseViewSet):
    queryset = Requisite.objects.all()
    pagination_class = RequestPagination
    serializer_class = RequisiteReadSerializer


class PaymentRequestViewSet(BaseViewSet):
    queryset = PaymentRequest.objects.all()
    pagination_class = RequestPagination
    serializer_class = PaymentRequestReadSerializer

    @action(detail=True,
            methods=['get'],
            permission_classes=[permissions.AllowAny])
    def get_invoice_status(self, request, pk=None):

        serializer = PaymentRequestMiniSerializer(
            get_object_or_404(PaymentRequest, pk=pk))
        return Response(serializer.data)

    @action(detail=False,
            methods=['post'],
            permission_classes=[permissions.AllowAny])
    def create_invoice(self, request, pk=None):
        serializer = PaymentRequestWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
