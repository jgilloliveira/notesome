from api_rest.serializers import BaseModelSerializer
from apps.folders.models import Folder
from rest_framework import serializers


class ReadByIdField(serializers.Field):

  def __init__(self, serializer, *, read_only=False, write_only=False, required=None, default=None, initial=None, source=None, label=None, help_text=None, style=None, error_messages=None, validators=None, allow_null=False):
    super().__init__(read_only=read_only, write_only=write_only, required=required, default=default, initial=initial, source=source, label=label, help_text=help_text, style=style, error_messages=error_messages, validators=validators, allow_null=allow_null)
    self.serializer = serializer

  def to_representation(self, value):
    return self.serializer(value).data

  def to_internal_value(self, data):
    return self.serializer.Meta.model.objects.filter(id=data).first()


class ChildFolderSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())


  class Meta:
    model = Folder
    fields = '__all__'


class FolderSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  child_folders = ChildFolderSerializer(read_only=True, many=True)
  parent_folder = ReadByIdField(ChildFolderSerializer)
  url = serializers.ReadOnlyField()

  class Meta:
    model = Folder
    fields = '__all__'
