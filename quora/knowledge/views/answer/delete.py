from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from knowledge.models.answer import Answer
from users.models import User

class AnswerDelete(LoginRequiredMixin, DeleteView):
    model = Answer
    def get_success_url(self):
        question_id = self.kwargs['question']
        return reverse_lazy('question-detail', args=[str(question_id)])