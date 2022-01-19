import logging

# Create your views here.
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Proverb
from .serializers import ProverbSerializer


class ProverbListAPIView(ListAPIView):
    """This endpoint list all of the available proverbs from the database"""

    queryset = Proverb.objects.all().order_by('proverb')
    serializer_class = ProverbSerializer


class CreateProverbAPIView(CreateAPIView):
    """This endpoint allows for creation of a proverb"""
    queryset = Proverb.objects.all()
    serializer_class = ProverbSerializer


class UpdateProverbAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific proverb by passing in the id of the proverb to update"""
    queryset = Proverb.objects.all()
    serializer_class = ProverbSerializer


class DeleteProverbAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific proverb from the database"""
    queryset = Proverb.objects.all()
    serializer_class = ProverbSerializer


class ServiceUnavailable(APIException):
    logger = logging.getLogger('HttpResponse')
    method_not_allowed, bad_request = (405, 400)
    if method_not_allowed:
        logger.error("Unexpected error occurred %s", "major problem", exc_info=1)
    elif bad_request:
        logger.error(2, 'Please input correct data')
