from rest_framework import serializers
from django.contrib.auth.models import Group, User
from book_issue.serializers import *
from userprofile.models import *
from datetime import datetime

class ProfileSerializer(serializers.ModelSerializer):
    books_issue = IssueSerializer(many=True)
    fine = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ('employee_id', 'email', 'fine', 'books_issue')

    def get_fine(self, profile):
        # import pdb
        # pdb.set_trace()
        import pytz
        utc = pytz.UTC
        today = datetime.now()
        today = utc.localize(today)
        books_issued = profile.books_issue.all()
        fine = 0
        for book_issued in books_issued:
            # book_issued.return_date = utc.localize(book_issued.return_date)
            return_date = book_issued.return_date
            exceeded_days = 1
            book_fine = 0
            if today > return_date:
                exceeded_days = (today - return_date).days
                book_fine = exceeded_days * 10
            fine += book_fine
        return fine
