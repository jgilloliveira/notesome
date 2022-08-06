from api_rest.views import BaseModelViewSet
from apps.users.serializers import UserSerializer



class UserView(BaseModelViewSet):
  serializer_class = UserSerializer

  
