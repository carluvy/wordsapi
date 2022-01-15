from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from .models import Word
from .serializers import WordSerializer

#
# class WordViewSet(viewsets.ModelViewSet):
#     queryset = Word.objects.all().order_by('word')
#     serializer_class = WordSerializer


class WordListAPIView(ListAPIView):
    """This endpoint list all of the available words from the database"""
    queryset = Word.objects.all().order_by('word')
    serializer_class = WordSerializer


class CreateWordAPIView(CreateAPIView):
    """This endpoint allows for creation of a word"""
    queryset = Word.objects.all()
    # lower_case = str(queryset).upper()
    serializer_class = WordSerializer


class UpdateWordAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific word by passing in the id of the word to update"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class DeleteWordAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific word from the database"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer
