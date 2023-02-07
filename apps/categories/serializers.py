from unittest.util import _MAX_LENGTH
from api_rest.serializers import BaseModelSerializer
from apps.categories.models import Category
from rest_framework import serializers


class CategorySerializer(BaseModelSerializer):
  
  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  initials = serializers.ReadOnlyField()


  class Meta:
    model = Category
    fields = '__all__'

  def validate_name(self, value):
    if len(value.trim()) == 0:
      raise serializers.ValidationError("El campo no puede quedar vacío. ")
    return value
  