from api_rest.views import BaseModelViewSet
from apps.folders.serializers import FolderSerializer


class FolderView(BaseModelViewSet):
  serializer_class = FolderSerializer

  def get_queryset(self):
    return self.request.user.folders.all()
  