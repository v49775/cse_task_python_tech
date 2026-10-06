
from django.urls import path, include
from .views import create_job

urlpatterns = [
    path('jobs/', create_job.as_view(), name='create_job'),
    path('jobs/<int:job_id>/', create_job.as_view(), name='get_jobs'),
]
