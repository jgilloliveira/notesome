from api_rest.views import BaseModelViewSet
from apps.notes.serializers import NoteSerializer

from rest_framework.permissions import IsAuthenticated


class NoteView(BaseModelViewSet):
  serializer_class = NoteSerializer

  def get_queryset(self):  
    return self.request.user.notes.all()
  



