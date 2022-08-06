from django.db import models
from api_rest.models import BaseModel


class Note (BaseModel):
  title = models.TextField()
  content = models.TextField()
  color = models.CharField(max_length=10)
  is_favorite = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)

  parent_folder = models.ForeignKey("folders.Folder", verbose_name="parent_folder", null=True, blank=True, on_delete=models.CASCADE)
  categories = models.ManyToManyField("categories.Category", verbose_name="categories", blank=True)

