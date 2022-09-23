from django.contrib import admin
from apps.users.models import User

# Register your models here.
@admin.register(User)
class InvitationAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'username',
  )