from django.db import models

# Create your models here.
class TumorDetection(models.Model):
    originalImg = models.ImageField(upload_to='oimgs')
    processedImg = models.ImageField(upload_to='processedImg')
