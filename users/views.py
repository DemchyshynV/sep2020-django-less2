from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserModel
from .serializers import UserSerializer


# create POST
# read GET
# update PUT/PATCH
# delete DELETE
class ListCreateView(APIView):
    def get(self, *args, **kwargs):
        qs = UserModel.objects.all()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(name__iexact=name)
        # qs = UserModel.objects.all().filter(name__iexact='max').filter(age__gt=15).exclude(gender__startswith='m')
        # qs = qs.filter(na='max')
        # qs =qs.filter(age__gt=15)
        # print(qs)
        # get = UserModel.objects.get(name='Max')
        # all_ = UserModel.objects.all()[::2]

        users = UserSerializer(qs, many=True).data
        return Response(users, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # user = UserModel.objects.get(pk=pk)
        user = get_object_or_404(UserModel, pk=pk)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        # pk = kwargs.get('pk')
        intance = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(intance, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# class UserView(APIView):

# def get(self, *args, **kwargs):
#     return Response('hello from get')
#
# def post(self, *args, **kwargs):
#     return Response('hello from post')
#
# def put(self, *args, **kwargs):
#     return Response('hello from put')
#
# def patch(self, *args, **kwargs):
#     return Response('hello from patch')
#
# def delete(self, *args, **kwargs):
#     return Response('hello from delete')
