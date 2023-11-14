from django.db import models


# Create your models here.
class Work(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
