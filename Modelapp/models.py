from django.db import models

from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'
