from django.contrib import admin
from apps.notes.models import Note

# Register your models here.
#admin.site.register(Note)
@admin.register(Note)
class InvitationAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'title',
    'content',
    'color',
    'user',
  )