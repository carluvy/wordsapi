# Create your views here.
from django.db import IntegrityError
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

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


class CreateWordAPIView(CreateAPIView):
    """This endpoint allows for creation of a word"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    # def post(self, request):
    #     word = request.data
    #     serializer = self.serializer_class(data=word)
    #     serializer.is_valid(raise_exception=True)
    #     # serializer.save()
    #     try:
    #         words = Word.objects.create(word=serializer.data.get('word'), definition=request.data.get('definition') )
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


class UpdateWordAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific word by passing in the id of the word to update"""
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "word updated successfully"})

        else:
            return Response({"message": "failed", "details": serializer.errors})


class DeleteWordAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific word from the database"""
    queryset = Word.objects.all().order_by('word')
    serializer_class = WordSerializer
