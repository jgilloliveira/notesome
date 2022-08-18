from api_rest.serializers import BaseModelSerializer
from apps.folders.models import Folder
from rest_framework import serializers


class ChildFolderSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())

  class Meta:
    model = Folder
    fields = '__all__'


class FolderSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  child_folders = ChildFolderSerializer(read_only=True, many=True)


  class Meta:
    model = Folder
    fields = '__all__'
    