from django.db import models

# Create your models here.


class jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    priority= models.IntegerField()
    status= models.CharField(max_length=100, default='queued')
    