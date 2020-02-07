from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# from .forms import CreateQuestion
# Create your views here.

from .models import Question, Answer, Comment
from users.models import User

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


class AnswerCreate(LoginRequiredMixin, CreateView):
    model = Answer
    fields = '__all__'
    

class AnswerUpdate(LoginRequiredMixin, UpdateView):
    model = Answer
    fields = '__all__'

class AnswerDelete(LoginRequiredMixin, DeleteView):
    model = Answer
    success_url = reverse_lazy('answers')


class UserUpdate(LoginRequiredMixin, UpdateView):
    model=User
    fields=['firstname', 'lastname', 'bio']

class UserDelete(LoginRequiredMixin, DeleteView):
    model=User
    success_url = reverse_lazy('index')

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_text']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.pub_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        print(initial)
        initial['pub_date'] = timezone.now()
        print(initial)

        return initial

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super(QuestionCreate, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['user'] = self.request.user
    #     return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pub_date'] = timezone.now()
    #     context['user'] = self.request.user
    #     return context
class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = '__all__'

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('questions')

class CommentCreate(LoginRequiredMixin, CreateView):
    model=Comment
    fields='__all__'

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model=Comment
    fields=['comment_text']

class CommentDelete(LoginRequiredMixin, DeleteView):
    model=Comment
    success_url = reverse_lazy('question-detail')

