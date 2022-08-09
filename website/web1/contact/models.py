from django.db import models

class contact(models.Model):
     contact_name = models.CharField(max_length=50)
     contact_email = models.EmailField()
     contact_comment=models.TextField()
     
# Create your models here.
