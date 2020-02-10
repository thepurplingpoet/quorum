from django.shortcuts import render, get_object_or_404, redirect
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
        question = Question.objects.get(pk=question_id)
        self.object.question = question
        self.object.user = self.request.user
        self.object.pub_date = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy('question-detail', args=[str(question_id)])
        return HttpResponseRedirect(self.get_success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs['question']
        question = Question.objects.get(pk=question_id)
        context['question'] = question.question_text
        return context

class AnswerUpdate(LoginRequiredMixin, UpdateView):
    model = Answer
    fields = ['answer_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        question_id = self.kwargs['question']
        self.object.question = Question.objects.get(pk=question_id)
        self.object.user = self.request.user
        self.object.updated = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy('answer-detail', args=[str(question_id), self.object.pk])
        return HttpResponseRedirect(self.get_success_url)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs['question']
        question = Question.objects.get(pk=question_id)
        context['question'] = question.question_text
        return context

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer_id = self.kwargs['answer']
        answer = Answer.objects.get(pk=answer_id)
        context['answer'] = answer.answer_text[:50]
        return context
        
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer_id = self.kwargs['answer']
        answer = Answer.objects.get(pk=answer_id)
        context['answer'] = answer.answer_text[:50]
        return context

class CommentDelete(LoginRequiredMixin, DeleteView):
    model=Comment
    def get_success_url(self):
        question_id = self.kwargs['question']
        answer_id = self.kwargs['answer']
        return reverse_lazy('answer-detail', args=[str(question_id), str(answer_id)])

def question_vote(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        user = request.user
        if "upvote" in request.POST:
            question.upvotes+=1
            question.upvote_users.add(user)
            question.save()
        elif "downvote" in request.POST:
            question.downvotes+=1
            question.downvote_users.add(user)
            question.save()
        elif "remove_upvote" in request.POST:
            question.upvotes-=1
            question.upvote_users.remove(user)
            question.save()
        elif "remove_downvote" in request.POST:
            question.downvotes-=1
            question.downvote_users.remove(user)
            question.save()

        
    return redirect('question-detail', pk)

def answer_vote(request, question, pk):
    answer = get_object_or_404(Answer, pk=pk)

    if request.method == 'POST':
        user = request.user
        if "upvote" in request.POST:
            answer.upvotes+=1
            answer.upvote_users.add(user)
            answer.save()
        elif "downvote" in request.POST:
            answer.downvotes+=1
            answer.downvote_users.add(user)
            answer.save()
        elif "remove_upvote" in request.POST:
            answer.upvotes-=1
            answer.upvote_users.remove(user)
            answer.save()
        elif "remove_downvote" in request.POST:
            answer.downvotes-=1
            answer.downvote_users.remove(user)
            answer.save()

        
    return redirect('answer-detail', question , pk)

def comment_vote(request, question, answer, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        user = request.user
        if "upvote" in request.POST:
            comment.upvotes+=1
            comment.upvote_users.add(user)
            comment.save()
        elif "downvote" in request.POST:
            comment.downvotes+=1
            comment.downvote_users.add(user)
            comment.save()
        elif "remove_upvote" in request.POST:
            comment.upvotes-=1
            comment.upvote_users.remove(user)
            comment.save()
        elif "remove_downvote" in request.POST:
            comment.downvotes-=1
            comment.downvote_users.remove(user)
            comment.save()

        
    return redirect('answer-detail', question , answer)