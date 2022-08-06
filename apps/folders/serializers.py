from api_rest.serializers import BaseModelSerializer
from apps.folders.models import Folder


class FolderSerializer(BaseModelSerializer):
  class Meta:
    model = Folder
    fields = '__all__'
