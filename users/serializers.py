from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from cars.serializers import CarSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    cars = CarSerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'is_superuser', 'is_staff', 'is_active', 'cars']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user
