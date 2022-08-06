from rest_framework import serializers
from apps.users.models import User
from api_rest.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):

  class Meta:
    model = User
    fields = '__all__'
