from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import User, Question, Answer, Comment

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_users = User.objects.all().count()
    num_questions = Question.objects.all().count()

    
    context = {
        'num_questions': num_questions,
        'num_users': num_users
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class QuestionList(generic.ListView):
    model = Question

class UserList(generic.ListView):
    model = User

class QuestionDetail(generic.DetailView):
    model = Question


class UserDetail(generic.DetailView):
    model = User
