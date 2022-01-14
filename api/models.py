from django.db import models


# Create your models here.

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    definition = models.CharField(max_length=50)

    def __str__(self):
        return self.word
