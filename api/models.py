from django.db import models, IntegrityError

# Create your models here.
from django.forms import forms
from rest_framework.exceptions import ValidationError


class Word(models.Model):
    # id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=20, blank=False, null=False)
    state = models.CharField(max_length=10, blank=False, null=False)
    definition = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.word
