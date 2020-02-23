from rest_framework import serializers
from django.contrib.auth.models import Group, User
from book_issue.models import BookIssue

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookIssue
        fields = ('id','book','profile','issue_date','return_date')
