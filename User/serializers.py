from rest_framework import serializers

from djoser.serializers import UserCreateSerializer, UserSerializer

from User.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['email', 'phoneNumber', 'first_name', 'last_name']


class CurrentUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']