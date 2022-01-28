from rest_framework import serializers

from .models import Proverb


class ProverbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proverb
        fields = ['proverb', 'meaning']



