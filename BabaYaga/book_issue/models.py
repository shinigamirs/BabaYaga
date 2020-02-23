from django.db import models
from datetime import datetime, timedelta
import uuid
from userprofile.models import UserProfile
from library.models import Book

def get_uuid():
    return str(uuid.uuid4())


class BookIssue(models.Model):
    book = models.ForeignKey('library.Book',on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfile, related_name='books_issue', on_delete=models.CASCADE)
    issue_uuid = models.CharField(('uuid'), max_length=36, unique=True,
                default=get_uuid, editable=False)
    issue_date = models.DateTimeField(('issue date'),default=datetime.now)
    return_date = models.DateTimeField(('return date'),default=datetime.now()+timedelta(days=30))
    fine_amount = models.IntegerField(default=0)
