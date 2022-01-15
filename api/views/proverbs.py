from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ..models import Proverb
from ..serializers import ProverbSerializer


class ProverbListAPIView(ListAPIView):
    """This endpoint list all of the available proverbs from the database"""
    queryset = Proverb.objects.all().order_by('proverb')
    serializer_class = ProverbSerializer


class CreateProverbAPIView(CreateAPIView):
    """This endpoint allows for creation of a proverb"""
    queryset = Proverb.objects.all()
    # lower_case = str(queryset).upper()
    serializer_class = ProverbSerializer


class UpdateProverbAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific proverb by passing in the id of the proverb to update"""
    queryset = Proverb.objects.all()
    serializer_class = ProverbSerializer


class DeleteProverbAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific proverb from the database"""
    queryset = Proverb.objects.all()
    serializer_class = ProverbSerializer
