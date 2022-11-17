from email.policy import default
from api_rest.serializers import BaseModelSerializer
from apps.notes.models import Note
from rest_framework import serializers
from apps.categories.serializers import CategorySerializer


class NoteSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  categories = CategorySerializer(many=True, required=False)

  class Meta:
    model = Note
    fields = '__all__'
