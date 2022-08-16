from unittest.util import _MAX_LENGTH
from api_rest.serializers import BaseModelSerializer
from apps.categories.models import Category
from rest_framework import serializers


class CategorySerializer(BaseModelSerializer):
  
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())


  class Meta:
    model = Category
    fields = '__all__'

  
