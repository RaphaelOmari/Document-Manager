

def validate_file_type(upload):
    allowed_mime_types = ['application/pdf', 'image/jpeg']
    if upload.content_type not in allowed_mime_types:
        raise ValidationError('Unsupported file type.')

def validate_file_size(upload):
    max_size = 1024*1024*5
    if upload.size > max_size:
        raise ValidationError('File too large. Size should not exceed 5 MB.')