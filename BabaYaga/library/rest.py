from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from library.models import *
from library.serializers import *
from lib.decorator import *
import isbnlib

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = ('id')


class BookAddIsbn(APIView):

    @swagger_auto_schema(request_body=BookSerializer)
    @rest_process_exception
    def post(self, request, isbn=None):
        data = request.data
        try:
            if isbn:
                isbn_no = isbn
            else:
                isbn_no = data["isbn"]
            if isbnlib.is_isbn13(isbn_no):
                book_data = isbnlib.meta(isbn_no)
            else:
                raise("ISBN no. is not right")

        except Exception:
            raise("No data for this ISBN you can still add data manually"
                  "Use '/library/rest/book/' ")

        try:
            print(book_data)
            book = Book.objects.get(isbn=book_data.get("ISBN-13"))
            book.total_count = book.total_count + 1
            book.available_count = book.available_count + 1
            book.save()
            return Response(status=status.HTTP_201_CREATED)

        except Exception:
            book = Book()
            book.isbn = book_data.get("ISBN-13")
            book.title = book_data.get("Title")
            book.year = book_data.get("Year")
            book.save()

        authors = book_data.get("Authors")

        for name in authors:
            try:
                author = Author.objects.get(name=name)
                author.save()
                author.book.add(book)
                author.save()

            except Exception:
                author = Author()
                author.name = name
                author.save()
                author.book.add(book)
                author.save()
        if isbn:
            return
        return Response(status=status.HTTP_201_CREATED)

class BookAdd(APIView):

    @rest_process_exception
    def post(self, request):
        data = request.data
        try:
            try:
                book = Book.objects.get(isbn=data.get("isbn"))
                book.total_count = book.total_count + 1
                book.available_count = book.available_count + 1
                book.save()
                return Response(status=status.HTTP_201_CREATED)

            except Exception:
                book = Book()
                book.isbn = data.get("isbn")
                book.title = data.get("title")
                book.year = data.get("year")
                book.save()

            authors = data.get("authors")

            for name in authors:

                try:
                    author = Author.objects.get(name=name)
                    author.save()
                    author.book.add(book)
                    author.save()

                except Exception:
                    author = Author()
                    author.name = data.get("author")
                    author.save()
                    author.book.add(book)
                    author.save()

        except Exception as e:
            raise e

class BulkBookAddIsbn(APIView):

    @rest_process_exception
    def post(self, request):
        try:
            fail_list = []
            list = request.data.get("isbn_list")
            for isbn in list:
                api = BookAddIsbn()
                try:
                    api.post(request,isbn)
                except Exception:
                    fail_list.append(isbn)

            result = {"fail_list" : fail_list}
            return Response(result, status=status.HTTP_201_CREATED)

        except Exception as e:
            raise e