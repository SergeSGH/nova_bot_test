from django.urls import path

from .views import OnePageView, CleanData

urlpatterns = (
    path('', OnePageView, name='index'),
    path('clean_data/', CleanData, name='cleandata'),
)
