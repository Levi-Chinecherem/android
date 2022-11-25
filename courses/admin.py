from django.contrib import admin
from .models import *

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  list_display = ("title", "video_url", "date_created")
  list_filter = ['date_created']
  search_fields = ['title', 'date_created']

