from django.urls import path

from .views import CleanData, OnePageView

urlpatterns = (
    path('', OnePageView, name='index'),
    path('clean_data/', CleanData, name='cleandata'),
)
