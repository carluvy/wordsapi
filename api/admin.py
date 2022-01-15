from django.contrib import admin

# Register your models here.
from .models import Word, Proverb

admin.site.register(Word)
admin.site.register(Proverb)
