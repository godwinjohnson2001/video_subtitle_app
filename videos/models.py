from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='subtitles')
    language = models.CharField(max_length=50, default='English')  # For multi-language support
    content = models.TextField()
    subtitle_file = models.FileField(upload_to='subtitles/', blank=True, null=True)
   

    def __str__(self):
        return f"{self.language} - {self.video.title}"

