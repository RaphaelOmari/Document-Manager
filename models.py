from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
class FileRevision(models.Model):
    file = models.ForeignKey(File, related_name='revisions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    file_content = models.FileField(upload_to='files/')

    def __str__(self):
        return f"{self.file.name} - Revision {self.version}"