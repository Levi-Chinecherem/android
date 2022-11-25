from django.shortcuts import render
from .models import *

# Create video view
def videos_view(request):
  videos = Video.objects.all()
  context = {
    "videos": videos,
  }
  return render(request, "index.html", context)

# Create details view for videos
def video_details_view(request, title):
  vid = Video.objects.get(title=title)
  
  context = {
    "vid": vid,
  }
  return render(request, "video_details.html", context)
