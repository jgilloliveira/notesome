from api_rest.serializers import BaseModelSerializer
from apps.notes.models import Note


class NoteSerializer(BaseModelSerializer):
  class Meta:
    model = Note
    fields = '__all__'
