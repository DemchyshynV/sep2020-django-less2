from django.urls import path

from .views import CarsListView
urlpatterns = [
    path('', CarsListView.as_view(), name='cars_list')
]
