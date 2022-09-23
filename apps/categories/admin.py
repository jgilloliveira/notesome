from django.contrib import admin
from apps.categories.models import Category

# Register your models here.
#admin.site.register(Note)
@admin.register(Category)
class InvitationAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'name',
    'user',
  )