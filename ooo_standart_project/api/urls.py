from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('requisites', views.RequisiteViewSet)
router.register('invoices', views.PaymentRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
