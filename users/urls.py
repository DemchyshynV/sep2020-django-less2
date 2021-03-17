from django.urls import path

from .views import UserListCreateView, AddProfileView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>/profile', AddProfileView.as_view(), name='users_add_profile')
]
