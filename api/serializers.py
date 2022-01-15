from rest_framework import serializers

from .models import Word, Proverb


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word', 'state', 'definition']


class ProverbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proverb
        fields = ['__all__']
