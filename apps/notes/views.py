from api_rest.views import BaseModelViewSet
from apps.notes.serializers import NoteSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class NoteView(BaseModelViewSet):
  serializer_class = NoteSerializer
  # filterset_fields = ['categories', 'folder']
  filterset_fields = {'categories': ['exact'], 'folder': ['exact', 'isnull']}
  filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
  search_fields = ['title', 'content']
  ordering_fields = ['creation_date', 'modified_date', 'title', 'content']

  def get_queryset(self):  
    return self.request.user.notes.all()
