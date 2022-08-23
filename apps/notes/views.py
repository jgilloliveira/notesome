from api_rest.views import BaseModelViewSet
from apps.notes.serializers import NoteSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
#from rest_framework import filters


# TODO: Obtener notas dada una categoría
class NoteView(BaseModelViewSet):
  serializer_class = NoteSerializer
  #filter_backends = [filters.SearchFilter]
  fields = {
    'categories': ['contains'],
    #'folders': ['contains'],
    }

  def get_queryset(self):  
    return self.request.user.notes.all()
