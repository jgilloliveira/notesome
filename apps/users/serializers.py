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
      raise serializers.ValidationError({
        "error": "El usuario no existe o la contraseña es incorrecta. :c",
        # "username": "El usuario no existe o la contraseña es incorrecta. :c",
        # "password": "El usuario no existe o la contraseña es incorrecta. :c",
      })
    if not user.is_active:
      raise serializers.ValidationError({
        "username": "El usuario no está activo.",
      })

    self.context['user'] = user
    return data

  def create(self, data):
    user = self.context.get('user')
    token, _ = Token.objects.get_or_create(user=user)
    return user, token.key
  
  
class RegisterSerializer(serializers.Serializer):
  username = serializers.CharField(min_length=4, max_length=16)
  password = serializers.CharField(min_length=4, max_length=64)
  password_confirm = serializers.CharField(min_length=4, max_length=64)

  def validate(self, data):
    user_exists = User.objects.filter(username=data.get('username')).exists()
    
    if user_exists:
      raise serializers.ValidationError({
        'username': 'El nombre de usuario ya existe.'
      })

    if data.get("password") != data.get("password_confirm"):
      raise serializers.ValidationError({
        'password_confirm': 'Las contraseñas no coinciden.'
      })
    
    return data

  def create(self, data):
    user = User(username=data.get('username'))
    user.set_password(data.get('password'))
    user.save()
    return user
