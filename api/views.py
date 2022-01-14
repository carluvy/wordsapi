from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Word
from .serializers import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all().order_by('word')
    serializer_class = WordSerializer
