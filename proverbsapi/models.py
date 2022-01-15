from django.db import models


# Create your models here.

class Proverb(models.Model):
    id = models.AutoField(primary_key=True)
    proverb = models.TextField()
    meaning = models.TextField()

    def __str__(self):
        return self.proverb
