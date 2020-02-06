from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime
# from .forms import CreateQuestion
# Create your views here.

from .models import User, Question, Answer, Comment

def index(request):
    """View function for home page of site."""

    latest_questions = Question.objects.all()[:5]

    
    context = {
        'questions':latest_questions
    }

    return render(request, 'index.html', context=context)


class QuestionList(generic.ListView):
    model = Question

class UserList(generic.ListView):
    model = User

class QuestionDetail(generic.DetailView):
    model = Question


class UserDetail(generic.DetailView):
    model = User


class AnswerCreate(CreateView):
    model = Answer
    fields = '__all__'
    

class AnswerUpdate(UpdateView):
    model = Answer
    fields = '__all__'

class AnswerDelete(DeleteView):
    model = Answer
    success_url = reverse_lazy('answers')

class UserCreate(CreateView):
    model=User
    fields='__all__'

class UserUpdate(UpdateView):
    model=User
    fields=['name', 'bio']

class UserDelete(DeleteView):
    model=User
    success_url = reverse_lazy('index')

class QuestionCreate(CreateView):
    model = Question
    fields = ['question_text']
    #initial = {'pub_date':'05/01/2018','user':User()}
class QuestionUpdate(UpdateView):
    model = Question
    fields = '__all__'

class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('questions')

class CommentCreate(CreateView):
    model=Comment
    fields='__all__'

class CommentUpdate(UpdateView):
    model=Comment
    fields=['comment_text']

class CommentDelete(DeleteView):
    model=Comment
    success_url = reverse_lazy('question-detail')

