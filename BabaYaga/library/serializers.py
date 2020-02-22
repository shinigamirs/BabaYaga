from rest_framework import serializers
from library.models import *

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id' ,'name',)

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'isbn', 'authors', 'title', 'year', 'total_count', 'available_count', )