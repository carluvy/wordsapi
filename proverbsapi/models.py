from django.db import models


# Create your models here.

class Proverb(models.Model):
    id = models.AutoField(primary_key=True)
    proverb = models.CharField(max_length=255)
    meaning = models.CharField(max_length=255)

    def __str__(self):
        return self.proverb
