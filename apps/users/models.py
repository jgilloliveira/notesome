from django.db import models
from django.contrib.auth.models import AbstractUser
from api_rest.models import BaseModel


class User(AbstractUser, BaseModel):
  pass