from email.policy import default
from api_rest.serializers import BaseModelSerializer
from apps.notes.models import Note
from rest_framework import serializers


class NoteSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())

  class Meta:
    model = Note
    fields = '__all__'
