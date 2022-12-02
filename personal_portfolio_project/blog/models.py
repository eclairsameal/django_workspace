from django.db import models

# Create your models here.
class Brlog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField