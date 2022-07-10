from django.urls import path
from .views import catch_incoming_message


urlpatterns = [
    path('tg-webhook/', catch_incoming_message)]
