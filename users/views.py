from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import UserModel
from .serializers import UserSerializer


class ListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = UserModel.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__iexact=name)
        return qs


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
