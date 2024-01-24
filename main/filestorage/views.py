from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import File, FileRevision
import bcrypt 

def validate_file_type(upload):
    allowed_mime_types = ['application/pdf', 'image/jpeg']
    if upload.content_type not in allowed_mime_types:
        raise ValidationError('Unsupported file type.')

def validate_file_size(upload):
    max_size = 1024*1024*5
    if upload.size > max_size:
        raise ValidationError('File too large. Size should not exceed 5 MB.')
    
@login_required
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        url = request.POST['url']
        try:
            validate_file_type(file)
            validate_file_size(file)

        except ValidationError as e:
            return HttpResponse(e.messages, status=400)
        except Exception as e:
            print(e)

    return render(request, 'upload.html')