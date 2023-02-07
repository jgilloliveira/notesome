from django.db import models
from api_rest.models import BaseModel


class Category (BaseModel):
  name = models.TextField()
  user = models.ForeignKey('users.User', related_name='categories', on_delete=models.CASCADE)
  
  @property
  def initials(self):
    words = self.name.split(" ")
    if len(words) >=2:
      return f"{words[0][0]}{words[1][0]}".upper()
    word = words[0]
    if len(word)>1:
      return word[:2].upper()
    else:
      return word[0].upper()

''' 
1) Lógica simple y relacionado al modelo -> En el modelo
2) Lógica compleja y relacionado al modelo -> En un servicio y en el modelo
3) Lógica simple y no relacionado al modelo -> En la vista
4) Lógica compleja y no relacionado al modelo -> En un servicio y en la vista
'''