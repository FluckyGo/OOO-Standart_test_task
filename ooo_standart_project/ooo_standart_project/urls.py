from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
