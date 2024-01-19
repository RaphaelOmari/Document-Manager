from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)

class FileRevision(models.Model):
    file = models.ForeignKey(File, related_name='revisions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_content = models.FileField(upload_to='files/')