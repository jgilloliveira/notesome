from django.db import models
from api_rest.models import BaseModel


class Category (BaseModel):
  name = models.TextField()
  user = models.ForeignKey('users.User', related_name='categories', on_delete=models.CASCADE)
