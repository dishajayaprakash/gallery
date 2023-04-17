from django.db import models
from django.utils import timezone

class gallery(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    image = models.ImageField(upload_to='image/')
    time = models.DateTimeField(default=timezone.now)