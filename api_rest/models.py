from django.db import models


class BaseModel(models.Model):
  id = models.AutoField(primary_key=True)

  creation_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True