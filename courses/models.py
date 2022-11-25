from django.db import models

# Creating models for Videos.
class Video(models.Model):
  id= models.AutoField(primary_key=True, null=False)
  category = models.CharField(max_length=200,)
  title = models.CharField(max_length=200,)
  video_url = models.CharField(max_length=500,)
  description = models.TextField(max_length=9999999999)
  thumbnail = models.ImageField(upload_to='Video_Thumbs', null=True, blank=True, verbose_name="Video Thumbs")
  date_created = models.DateField(null=True, blank=True, auto_now_add=True)
  date_updated = models.DateField(auto_now=True, null=True, blank=True)

  class Meta:
    ordering = ('-date_created',)

  def __str__(self):
    return f"Course - {self.title}"