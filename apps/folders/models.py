from nturl2path import url2pathname
from django.db import models
from api_rest.models import BaseModel


class Folder (BaseModel):
  name = models.TextField()
  parent_folder = models.ForeignKey("self", verbose_name="parent_folder", null=True, blank=True, on_delete=models.CASCADE, related_name='child_folders')
  user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='folders')

  @property
  def url(self) -> list:

    folder = self
    result = []
    while folder is not None:
      result.insert(0,{ 
        "id": folder.id, 
        "name": folder.name 
      })
      folder = folder.parent_folder
      
    return result

  # @property
  # def url(self) -> list(dict):
    
  #   def url_rec(folder: "Folder") -> list(dict):
  #     if (folder.parent_folder is None):
  #       return []

  #     return [
  #       *url_rec(folder.parent_folder), 
  #       { 
  #         "id": folder.id, 
  #         "name": folder.name 
  #       }
  #     ]

  #   return url_rec(self)
