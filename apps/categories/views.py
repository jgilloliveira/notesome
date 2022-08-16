from api_rest.views import BaseModelViewSet
from apps.categories.serializers import CategorySerializer


class CategoryView(BaseModelViewSet):
  serializer_class = CategorySerializer

  def get_queryset(self):
    return self.request.user.categories.all()

  # def create(self, request, *args, **kwargs):
  #   request.data['user'] = request.user.id
  #   return super().create(request, *args, **kwargs)