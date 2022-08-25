from api_rest.views import BaseModelViewSet
from apps.notes.serializers import NoteSerializer


class NoteView(BaseModelViewSet):
  serializer_class = NoteSerializer
  filterset_fields = ['categories', 'folder']

  def get_queryset(self):  
    return self.request.user.notes.all()
