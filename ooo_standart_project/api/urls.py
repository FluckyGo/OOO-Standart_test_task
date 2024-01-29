from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.views import UserViewSet
from .views import PaymentRequestViewSet, RequisiteViewSet, HomePage

router = DefaultRouter()
router.register('requisites', RequisiteViewSet)
router.register('requests', PaymentRequestViewSet)

app_name = 'api'

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('api/', include(router.urls)),
    # path('auth/', include('djoser.urls.authtoken')),
]
