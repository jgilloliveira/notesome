# Django y Rest Framework
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import serializers

# Models
from apps.users.models import User

# Utils
from api_rest.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):

  class Meta:
    model = User
    fields = '__all__'


class LoginSerializer(serializers.Serializer):

  username = serializers.CharField(min_length=4, max_length=16)
  password = serializers.CharField(min_length=4, max_length=64)

  def validate(self, data):
    user = authenticate(username=data.get('username'), password=data.get('password'))

    if user is None:
      raise serializers.ValidationError("El usuario no existe. :c")
    if not user.is_active:
      raise serializers.ValidationError("El usuario no está activo.")

    self.context['user'] = user
    return data

  def create(self, data):
    user = self.context.get('user')
    token, = Token.objects.get_or_create(user=user)
    return user, token.key
  
  