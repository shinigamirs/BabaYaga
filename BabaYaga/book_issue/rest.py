from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from datetime import datetime, timedelta

from library.models import *
from book_issue.models import *
from book_issue.serializers import *
from django.http import Http404
from userprofile import *

class IssueBook(APIView):

    def post(self,request,):
        try:
            data = request.data
            isbn = data['isbn']
            emp_id = data['emp_id']
            book=Book.objects.get(isbn=isbn)
            if book.available_count == 0:
                content = {
                    'Book': book.title, 'result': 'Not available'
                }
                return Response(content)
                #add status to above line

            profile = UserProfile.objects.get(employee_id=emp_id)
            books_issue = profile.books_issue.filter(book=book)
            if books_issue.count() >= 1:
                content = {
                    'Book': book.title, 'result': 'You already have one copy of this book'
                }
                return Response(content)
            issue = BookIssue()
            issue.profile = profile
            issue.book = book
            issue.save()
            book.available_count -= 1
            book.save()

        except BookIssue.DoesNotExist:
            raise Http404("BookIssue : Book not found")

        except UserProfile.DoesNotExist:
            raise Http404("Userprofile : profile not found")

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


class ReturnBook(APIView):

    def delete(self,request):
        try:
            data = request.data
            isbn = data['isbn']
            emp_id = data['emp_id']
            book=Book.objects.get(isbn=isbn)
            profile = UserProfile.objects.get(employee_id=emp_id)
            book_issued = profile.books_issue.get(book=book)
            update_fine_amount(profile,book_issued)
            book_issued.delete()
            book.available_count += 1
            book.save()

        except BookIssue.DoesNotExist:
            raise Http404("BookIssue : Book not found")

        except UserProfile.DoesNotExist:
            raise Http404("Userprofile : profile not found")

        except Exception as e:
            raise e

        content = {
            'Book': book.title, 'result': 'Returned successfully'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)









