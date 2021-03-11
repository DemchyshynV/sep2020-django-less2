from django.urls import path

from .views import UserListCreateView, CarCreate

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>/cars', CarCreate.as_view(), name='useers_car_create')
]
