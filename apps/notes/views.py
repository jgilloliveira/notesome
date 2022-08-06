from api_rest.views import BaseModelViewSet
from apps.notes.serializers import NoteSerializer


class NoteView(BaseModelViewSet):
  serializer_class = NoteSerializer