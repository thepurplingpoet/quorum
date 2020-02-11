from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from knowledge.models.comment import Comment

class CommentDelete(LoginRequiredMixin, DeleteView):
    model=Comment
    def get_success_url(self):
        question_id = self.kwargs['question']
        answer_id = self.kwargs['answer']
        return reverse_lazy('answer-detail', args=[str(question_id), str(answer_id)])
