from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.email