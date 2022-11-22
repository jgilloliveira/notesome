from email.policy import default
from api_rest.serializers import BaseModelSerializer
from apps.categories.models import Category
from apps.notes.models import Note
from rest_framework import serializers
from apps.categories.serializers import CategorySerializer


class NoteSerializer(BaseModelSerializer):

  user = serializers.HiddenField(default=serializers.CurrentUserDefault())
  categories = CategorySerializer(many=True, required=False, read_only=True)
  new_categories = serializers.ListField(required=False, write_only=True, source="categories")

  class Meta:
    model = Note
    fields = '__all__'
