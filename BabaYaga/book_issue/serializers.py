from rest_framework import serializers
from django.contrib.auth.models import Group, User
from book_issue.models import BookIssue

class IssueSerializer(serializers.ModelSerializer):
    Book = serializers.SerializerMethodField()
    class Meta:
        model = BookIssue
        fields = ('id','book', 'Book', 'profile','issue_date','return_date')

    def get_Book(self,issue):
        return issue.book.title
