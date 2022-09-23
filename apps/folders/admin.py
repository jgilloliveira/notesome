from django.contrib import admin
from apps.folders.models import Folder

# Register your models here.
#admin.site.register(Note)
@admin.register(Folder)
class InvitationAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'name',
    'parent_folder',
    'user',
  )