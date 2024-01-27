from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.views import UserViewSet
from .views import PaymentRequestViewSet, RequisiteViewSet

router = DefaultRouter()
router.register('requisites', RequisiteViewSet)
router.register('requests', PaymentRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/', include('djoser.urls.authtoken')),
]
