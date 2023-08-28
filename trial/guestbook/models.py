from django.db import models

# Create your models here.

class Guests(models.Model):
    Guestname = models.TextField()
    time = models.DateTimeField()