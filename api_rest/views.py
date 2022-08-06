from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
  def get_queryset(self):
    try:
      return super().get_queryset()
    except:
      return self.serializer_class.Meta.model.objects.all()