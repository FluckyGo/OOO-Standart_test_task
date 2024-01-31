from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.views import UserViewSet
from .views import (PaymentRequestViewSet, RequisiteViewSet,
                    PaymentPage, RequsitePage)

router = DefaultRouter()
router.register('requisites', RequisiteViewSet)
router.register('invoices', PaymentRequestViewSet)

app_name = 'api'

urlpatterns = [
    path('', PaymentPage.as_view(), name='payment'),
    path('requisite/', RequsitePage.as_view(), name='requisite'),
    path('api/', include(router.urls)),
    # path('auth/', include('djoser.urls.authtoken')),
]
