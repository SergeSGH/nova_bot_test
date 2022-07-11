from django.urls import path

from .views import bot_data

urlpatterns = [
    path('', bot_data)
]
