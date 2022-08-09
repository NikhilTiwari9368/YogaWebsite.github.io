from django.db import models

class services(models.Model):
    services_title = models.CharField(max_length=50)
    services_desc = models.TextField()
# Create your models here.
