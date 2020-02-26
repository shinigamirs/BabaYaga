from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from datetime import datetime, timedelta
from django.contrib.auth.models import User

from library.models import *
from book_issue.models import *
from book_issue.serializers import *
from django.http import Http404
from userprofile import *
from library.rest import BookAddIsbn
from lib.decorator import rest_process_exception

class IssueBook(APIView):

    @rest_process_exception
    def post(self,request,):
        try:
            data = request.data
            isbn = data['isbn']
            emp_id = data['emp_id']
            try:
                book = Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                book = BookAddIsbn().post(request, isbn)
                #add status to above line
            try:
                profile = UserProfile.objects.get(employee_id=emp_id)
            except UserProfile.DoesNotExist:
                email = request.data["email"]
                user = User()
                user.username = email
                user.save()
                profile = UserProfile()
                profile.user = user
                profile.employee_id = emp_id
                profile.save()

            books_issue = profile.books_issue.filter(book=book)
            if books_issue.count() >= 1:
                content = {
                    'Book': book.title, 'result': 'You already have one copy of this book'
                }
                return Response(content,status=status.HTTP_405_METHOD_NOT_ALLOWED)
            issue = BookIssue()
            issue.profile = profile
            issue.book = book
            issue.save()
            book.available_count -= 1
            book.save()


        except Exception as e:
            raise e
        serializer = IssueSerializer(issue,many=False)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

def update_fine_amount(profile,book_issued):
    import pytz
    utc = pytz.UTC
    # today = datetime.now()
    today = datetime.now()
    today = utc.localize(today)
    return_date = book_issued.return_date
    exceeded_days = 0
    if today > return_date:
        exceeded_days = (today-return_date).days
    book_fine = exceeded_days*10
    profile.fine_amount += book_fine
    profile.save()
    return book_fine


class ReturnBook(APIView):

    def delete(self,request):
        # import pdb
        # pdb.set_trace()
        try:
            data = request.data
            isbn = data['isbn']
            emp_id = data['emp_id']
            try:
                book=Book.objects.get(isbn=isbn)
            except Book.DoesNotExist:
                book = BookAddIsbn().post(request, isbn)
                content = {
                    'Book': book.title, 'result': 'You have not issued this book yet'
                }
                return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            try:
                profile = UserProfile.objects.get(employee_id=emp_id)
            except UserProfile.DoesNotExist:
                email = request.data["email"]
                user = User()
                user.username = email
                user.save()
                profile = UserProfile()
                profile.user = user
                profile.employee_id = emp_id
                profile.save()
                content = {
                    'Book': book.title, 'result': 'You have not issued this book yet'
                }
                return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            try:
                book_issued = profile.books_issue.get(book=book)
            except BookIssue.DoesNotExist:
                content = {
                    'Book': book.title, 'result': 'You have not issued this book yet'
                }
                return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            book_fine = update_fine_amount(profile,book_issued)
            book_issued.delete()
            book.available_count += 1
            book.save()

        except Exception as e:
            raise e

        content = {
            'Book': book.title, 'Book_Fine':book_fine, 'result': 'Returned successfully'
        }
        return Response(content, status=status.HTTP_200_OK)









