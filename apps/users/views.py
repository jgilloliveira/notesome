# dJANGO Y REST FRAMEWORK
from rest_framework.response import Response
from rest_framework.decorators import action
# Views
from api_rest.views import BaseModelViewSet
# Models
from apps.users.models import User
# Serializers
from apps.users.serializers import RegisterSerializer, UserSerializer, LoginSerializer


class UserView(BaseModelViewSet):
  serializer_class = UserSerializer

  @action(detail=False, methods=['post'])
  def login(self, request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user, token = serializer.save()
    data = {
      'user': UserSerializer(user).data,
      'token': token,
    }
    return Response(data)

  @action(detail=False, methods=['post'])
  def register(self, request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return self.login(request)

