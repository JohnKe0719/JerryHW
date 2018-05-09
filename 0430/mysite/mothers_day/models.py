from django.db import models

# Create your models here.
class postIt(models.Model):
    words=models.CharField(max_length=100)
    def __str__(self):
        return self.words

