from api_rest.views import BaseModelViewSet
from apps.categories.serializers import CategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class CategoryView(BaseModelViewSet):
  serializer_class = CategorySerializer
  filter_backends = [SearchFilter, OrderingFilter]
  search_fields = ["name"]
  ordering_fields = ['creation_date', 'modified_date', "name"]

  def get_queryset(self):
    return self.request.user.categories.all()

  # def create(self, request, *args, **kwargs):
  #   request.data['user'] = request.user.id
  #   return super().create(request, *args, **kwargs)

  # @action(detail=True, methods=['get'], url_name='notes')
  # def notes(self, request, pk):
  #   data = NoteSerializer(self.get_object().notes.all(), many=True).data
  #   return Response(data)