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


class AnswerDetail(generic.DetailView):
    model = Answer

class UserDetail(generic.DetailView):
    model = User


class AnswerCreate(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        question_id = self.kwargs['question']
        self.object.question = Question(question_id)
        self.object.user = self.request.user
        self.object.pub_date = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy('question-detail', args=[str(question_id)])
        return HttpResponseRedirect(self.get_success_url)

class AnswerUpdate(LoginRequiredMixin, UpdateView):
    model = Answer
    fields = ['answer_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        question_id = self.kwargs['question']
        self.object.question = Question(question_id)
        self.object.user = self.request.user
        self.object.updated = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy('question-detail', args=[str(question_id)])
        return HttpResponseRedirect(self.get_success_url)

class AnswerDelete(LoginRequiredMixin, DeleteView):
    model = Answer
    def get_success_url(self):
        question_id = self.kwargs['question']
        return reverse_lazy('question-detail', args=[str(question_id)])

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

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['question_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.updated = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class QuestionDelete(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('questions')

class CommentCreate(LoginRequiredMixin, CreateView):
    model=Comment
    fields=['comment_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        question_id = self.kwargs['question']
        answer_id = self.kwargs['answer']
        self.object.answer = Answer(answer_id)
        self.object.user = self.request.user
        self.object.pub_date = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy('answer-detail', args=[str(question_id), str(answer_id)])
        return HttpResponseRedirect(self.get_success_url)
        
class CommentUpdate(LoginRequiredMixin, UpdateView):
    model=Comment
    fields=['comment_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        question_id = self.kwargs['question']
        answer_id = self.kwargs['answer']
        self.object.answer = Answer(answer_id)
        self.object.user = self.request.user
        self.object.updated = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy('answer-detail', args=[str(question_id), str(answer_id)])
        return HttpResponseRedirect(self.get_success_url)

class CommentDelete(LoginRequiredMixin, DeleteView):
    model=Comment
    success_url = reverse_lazy('question-detail')

