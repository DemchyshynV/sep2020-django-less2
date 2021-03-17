from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, CreateAPIView, get_object_or_404

from user_profile.serializers import ProfileSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import UserSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AddProfileView(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        print(self.request.user)
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)
