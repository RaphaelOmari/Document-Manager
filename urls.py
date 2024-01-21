from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('fetch/<path:file_url>/', views.fetch_file, name='fetch_file'),
    path('fetch/<path:file_url>/<int:revision>/', views.fetch_file, name='fetch_file_revision'),
]