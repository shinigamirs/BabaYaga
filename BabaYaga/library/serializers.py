from rest_framework import serializers
from library.models import *

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name',)

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('isbn', 'authors', 'title', 'year', 'total_count', 'available_count', )