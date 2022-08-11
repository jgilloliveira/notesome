from django.db import models
from api_rest.models import BaseModel


class Note (BaseModel):
  title = models.TextField(blank="")
  content = models.TextField(blank="")
  color = models.CharField(max_length=10, default="#FFF")
  is_favorite = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)

  parent_folder = models.ForeignKey("folders.Folder", verbose_name="parent_folder", null=True, blank=True, on_delete=models.CASCADE)
  categories = models.ManyToManyField("categories.Category", verbose_name="categories", blank=True)
  user = models.ForeignKey("users.User", related_name='notes', on_delete=models.CASCADE)
