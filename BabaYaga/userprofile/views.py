from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect, render
from userprofile.models import UserProfile
from userprofile.serializers import ProfileSerializer

def login(request):

    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    books = profile.books_issue.all()
    name = user.first_name + " " + user.last_name
    fine = ProfileSerializer().get_fine(profile)
    context = {
        'name' : name,
        'user' : user,
        'book' : books,
        'fine' : fine
    }
    return render_to_response('home.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')