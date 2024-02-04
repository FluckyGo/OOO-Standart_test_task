from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from api.views import UserViewSet
from . import views

router = DefaultRouter()
router.register('requisites', views.RequisiteViewSet)
router.register('invoices', views.PaymentRequestViewSet)

app_name = 'api'

urlpatterns = [
    path(
        '',
        views.PaymentPage.as_view(),
        name='payment'
    ),
    path(
        'requisite/',
        views.RequsitePage.as_view(),
        name='requisite'
    ),
    path(
        'api/',
        include(router.urls)
    ),
    path(
        'profile/<str:username>/',
        views.UserProfileView.as_view(),
        name='profile'
    ),
    path(
        'profile/<str:username>/edit/',
        views.EditProfileView.as_view(),
        name='edit_profile'
    ),
    # path('auth/', include('djoser.urls.authtoken')),
]
