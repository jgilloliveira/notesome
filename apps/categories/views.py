from api_rest.views import BaseModelViewSet
from apps.categories.serializers import CategorySerializer
from apps.notes.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class CategoryView(BaseModelViewSet):
  serializer_class = CategorySerializer

  def get_queryset(self):
    return self.request.user.categories.all()

  # def create(self, request, *args, **kwargs):
  #   request.data['user'] = request.user.id
  #   return super().create(request, *args, **kwargs)

  @action(detail=True, methods=['get'], url_name='notes')
  def notes(self, request, pk):
    data = NoteSerializer(self.get_object().notes.all(), many=True).data
    return Response(data)