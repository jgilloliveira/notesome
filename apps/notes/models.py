from django.db import models
from api_rest.models import BaseModel
from rest_framework.exceptions import ValidationError

# TODO: Probar en postman parab saber si retorna un json con ValidationError

class Note (BaseModel):
  title = models.TextField(blank=True, default="")
  content = models.TextField(blank=True, default="")
  color = models.CharField(max_length=10, default="#FFFFFF")
  is_favorite = models.BooleanField(default=False)
  is_deleted = models.BooleanField(default=False)
  is_archived = models.BooleanField(default=False) 

  folder = models.ForeignKey("folders.Folder", related_name='notes', null=True, blank=True, on_delete=models.CASCADE)
  categories = models.ManyToManyField("categories.Category", blank=True, related_name='notes')
  user = models.ForeignKey("users.User", related_name='notes', on_delete=models.CASCADE)

  def validate(self):
    if self.is_deleted and self.is_favorite:
      raise ValidationError({"error": "La nota no puede estar eliminada y ser favorito."})
    elif self.is_deleted and self.is_archived:
      raise ValidationError({"error": "La nota no puede estar eliminada y archivado."})

  def save(self, *arg, **karg):
    self.validate()
    return super().save(*arg, **karg)