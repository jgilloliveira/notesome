from django.db import models
from api_rest.models import BaseModel


class Category (BaseModel):
  name = models.TextField()
