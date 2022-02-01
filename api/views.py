# Create your views here.
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.generic.base import logger
from rest_framework import permissions, status, generics
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

from . import serializers
from .models import Word
from .serializers import WordSerializer


#
# class WordViewSet(viewsets.ModelViewSet):
#     queryset = Word.objects.all().order_by('word')
#     serializer_class = WordSerializer


class WordListAPIView(ListAPIView):
    # for word in Word.objects.values_list('word', flat=True).distinct():
    # #     Word.objects.filter(pk__in=Word.objects.filter(word=word).values_list('id', flat=True)[1:]).delete()
    # for instance in Word.objects.values_list('word', 'definition'):
    #     if instance in Word.objects.values_list():
    #         raise IntegrityError("Word already exists")
    # raise forms.ValidationError(str('word') + ' already exists')

    """This endpoint list all of the available words from the database"""
    queryset = Word.objects.all().order_by('word')

    serializer_class = WordSerializer


class CreateWordAPIView(generics.ListCreateAPIView):
    """This endpoint allows for creation of a word"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    # def word_detail(self, request):
    #     word = request.data.get("pk")
    #     serializer = WordSerializer(word, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request):
    #     word = request.data
    #     serializer = self.serializer_class(data=word)
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     try:
    #         words = Word.objects.create(word=serializer.data.get('word'), definition=request.data.get('definition'))
    #         word_ = serializer.data.get('word')
    #         definition = serializer.data.get('definition')
    #         state = serializer.data.get('state')
    #     except IntegrityError:
    #         return Response('Word already exists', status=status.HTTP_406_NOT_ACCEPTABLE)
    #     msg = 'You have added the word {}, a {} that means {}.'.format(word_, state, definition)
    #
    #     # response = Response(msg)
    #
    #     return Response({'msg': msg})

    # response = JsonResponse(False, word, request)
    # return Response(word, status.HTTP_201_CREATED, False)


class UpdateWordAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint allows for updating a specific word by passing in the id of the word to update"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DeleteWordAPIView(RetrieveDestroyAPIView):
    """This endpoint allows for deletion of a specific word from the database"""
    queryset = Word.objects.all().order_by('word')
    serializer_class = WordSerializer
