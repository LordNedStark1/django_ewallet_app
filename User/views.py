from django.shortcuts import render
from djoser.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet

from User.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer