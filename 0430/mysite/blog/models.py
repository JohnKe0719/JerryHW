from django.db import models

# Create your models here.
class postIt(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

