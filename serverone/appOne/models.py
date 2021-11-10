from django.db import models

# Create your models here.
class Sample(models.Model):
    processed = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    