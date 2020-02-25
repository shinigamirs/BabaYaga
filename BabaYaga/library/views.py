from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from library.models import *
from django.views.generic import ListView
from django.core.paginator import Paginator
# # Create your views here.

# class PostListView(ListView):
#     model = Book
#     template_name = 'listing_books.html'
#     context_object_name = 'books'
#     ordering = ['title']
#     paginate_by = 2


def book_list(request, template_name="listing_books.html"):
    user = request.user
    name = user.first_name + " " + user.last_name
    books = Book.objects.all().order_by('title')
    paginator = Paginator(books, 4)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    context={
        'books' : books,
        'name' : name,
    }

    return render(request, template_name, context)

