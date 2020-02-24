from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from library.models import *

# Create your views here.
def book_list(request, template_name="listing_books.html"):
    user = request.user
    name = user.first_name + " " + user.last_name
    books = Book.objects.all()
    context={
        'books' : books,
        'name' : name,
    }
    return render(request, template_name, context)

