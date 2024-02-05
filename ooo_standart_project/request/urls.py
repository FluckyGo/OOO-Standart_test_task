from django.urls import path

from . import views

app_name = 'request'

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
        'search/',
        views.RequsitePage.as_view(),
        name='search'
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

]
