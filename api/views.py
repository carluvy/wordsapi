from django.db.models import Subquery, OuterRef, Count, Max

# Create your views here.
from django.db.models.functions import Upper
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from .models import Word
from .serializers import WordSerializer


#
# class WordViewSet(viewsets.ModelViewSet):
#     queryset = Word.objects.all().order_by('word')
#     serializer_class = WordSerializer


class WordListAPIView(ListAPIView):
    for word in Word.objects.values_list('word', flat=True).distinct():
        Word.objects.filter(pk__in=Word.objects.filter(word=word).values_list('id', flat=True)[1:]).delete()
    """This endpoint list all of the available words from the database"""
    queryset = Word.objects.all().order_by('word')

    serializer_class = WordSerializer


class CreateWordAPIView(CreateAPIView):
    """This endpoint allows for creation of a word"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class UpdateWordAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific word by passing in the id of the word to update"""
    get_id = Word.objects.values_list('id')

    queryset = Word.objects.all()
    serializer_class = WordSerializer


class DeleteWordAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific word from the database"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer
