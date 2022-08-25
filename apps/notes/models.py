from django.db import models
from api_rest.models import BaseModel


class Note (BaseModel):
  title = models.TextField(blank="")
  content = models.TextField(blank="")
  color = models.CharField(max_length=10, default="#FFF")
  is_favorite = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)

  folder = models.ForeignKey("folders.Folder", related_name='notes', null=True, blank=True, on_delete=models.CASCADE)
  categories = models.ManyToManyField("categories.Category", blank=True, related_name='notes')
  user = models.ForeignKey("users.User", related_name='notes', on_delete=models.CASCADE)
