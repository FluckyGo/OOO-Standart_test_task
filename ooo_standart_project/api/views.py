from rest_framework import permissions, viewsets
from django.views.generic import ListView

from .serializers import PaymentRequestReadSerializer, RequisiteReadSerializer
from request.models import Requisite, PaymentRequest
from .pagination import RequestPagination


class HomePage(ListView):
    template_name = 'request/index.html'
    model = PaymentRequest
    paginate_by = 10

    def get_queryset(self):
        return PaymentRequest.objects.select_related(
            'requisites'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment'] = PaymentRequest.objects.all
        return context


class RequisiteViewSet(viewsets.ModelViewSet):
    queryset = Requisite.objects.all()
    pagination_class = RequestPagination
    serializer_class = RequisiteReadSerializer

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve'):
    #         return RequisiteReadSerializer


class PaymentRequestViewSet(viewsets.ModelViewSet):
    queryset = PaymentRequest.objects.all()
    pagination_class = RequestPagination
    serializer_class = PaymentRequestReadSerializer

    # def get_serializer_class(self):
    #     if self.action in ('list', 'retrieve'):
    #         return PaymentRequestReadSerializer
