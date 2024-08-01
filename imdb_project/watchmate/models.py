from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=true)

    def __str__(self):
        return self.title