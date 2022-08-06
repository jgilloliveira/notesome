from api_rest.views import BaseModelViewSet
from apps.folders.serializers import FolderSerializer


class FolderView(BaseModelViewSet):
  serializer_class = FolderSerializer