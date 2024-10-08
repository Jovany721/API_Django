from django.db import models

# Create your models here.


class tabla_user(models.Model):

    nombre = models.CharField(max_length=90)
    edad = models.IntegerField()
    dpi = models.IntegerField()