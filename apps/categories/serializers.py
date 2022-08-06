from api_rest.serializers import BaseModelSerializer
from apps.categories.models import Category


class CategorySerializer(BaseModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'
