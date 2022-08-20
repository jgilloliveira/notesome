from api_rest.views import BaseModelViewSet
from apps.folders.serializers import ChildFolderSerializer, FolderSerializer


class FolderView(BaseModelViewSet):
  serializer_class = FolderSerializer

  def get_queryset(self):
    return self.request.user.folders.all()

  def get_serializer_class(self):
    if self.action == 'retrieve':
      return super().get_serializer_class()
    return ChildFolderSerializer