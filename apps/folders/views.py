from api_rest.views import BaseModelViewSet
from apps.folders.serializers import ChildFolderSerializer, FolderSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class FolderView(BaseModelViewSet):
  serializer_class = FolderSerializer
  filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
  # filterset_fields = ['parent_folder']
  filterset_fields = {'parent_folder': ['exact', 'isnull']}
  search_fields = ["name"]
  ordering_fields = ['creation_date', 'modified_date', "name"]

  def get_queryset(self):
    return self.request.user.folders.all()

  def get_serializer_class(self):
    if self.action == 'retrieve':
      return super().get_serializer_class()
    return ChildFolderSerializer

  