from .views import public_api
from django.urls import path

urlpatterns = [
    path('', public_api, name='public_api'),
]