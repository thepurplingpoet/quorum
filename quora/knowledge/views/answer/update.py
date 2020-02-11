from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from knowledge.models.answer import Answer
from knowledge.models.question import Question
from users.models import User
from django.http import HttpResponseRedirect


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
        self.get_success_url = reverse_lazy(
            'answer-detail', args=[str(question_id), self.object.pk])
        return HttpResponseRedirect(self.get_success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question_id = self.kwargs['question']
        question = Question.objects.get(pk=question_id)
        context['question'] = question.question_text
        return context
