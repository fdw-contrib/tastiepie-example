from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

