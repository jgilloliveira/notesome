from api_rest.views import BaseModelViewSet
from apps.categories.serializers import CategorySerializer


class CategoryView(BaseModelViewSet):
  serializer_class = CategorySerializer