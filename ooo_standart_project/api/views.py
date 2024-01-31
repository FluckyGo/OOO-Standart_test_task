from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, status

from .serializers import (PaymentRequestReadSerializer,
                          RequisiteReadSerializer,
                          PaymentRequestMiniSerializer,
                          PaymentRequestWriteSerializer)
from request.models import Requisite, PaymentRequest
from .pagination import RequestPagination
from .mixins import BaseViewSet


class PaymentPage(ListView):
    template_name = 'request/payment.html'
    model = PaymentRequest
    paginate_by = 10

    def get_queryset(self):
        return PaymentRequest.objects.select_related(
            'requisites'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RequsitePage(ListView):
    template_name = 'request/requsite.html'
    model = Requisite
    paginate_by = 10


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
