from rest_framework import serializers

from .models import Word


class WordSerializer(serializers.ModelSerializer):
    # word = serializers.SlugRelatedField(many=False, slug_field='word', queryset=Word.objects.all())

    class Meta:
        model = Word
        fields = ['word', 'state', 'definition']

