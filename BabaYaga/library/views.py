from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from library.models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
# # Create your views here.


def book_list(request, template_name="listing_books.html"):
    user = request.user
    name = user.first_name + " " + user.last_name
    page_number = request.GET.get('page')
    search_query = request.GET.get('search', '')
    books = Book.objects.all().order_by('title')
    if search_query:
        books = books.filter(Q(title__icontains=search_query) |
                            Q(isbn__icontains=search_query))
    paginator = Paginator(books, 4)
    books = paginator.get_page(page_number)
    context={
        'books' : books,
        'name' : name,
    }

    return render(request, template_name, context)

