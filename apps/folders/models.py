import re
from django.db import models
from api_rest.models import BaseModel


class Folder (BaseModel):
  name = models.TextField()
  parent_folder = models.ForeignKey("self", verbose_name="parent_folder", null=True, blank=True, on_delete=models.CASCADE, related_name='child_folders')
  user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='folders')
