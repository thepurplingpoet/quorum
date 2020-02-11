from django.views.generic.edit import CreateView
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from knowledge.models.comment import Comment
from knowledge.models.answer import Answer
from django.http import HttpResponseRedirect


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        question_id = self.kwargs['question']
        answer_id = self.kwargs['answer']
        self.object.answer = Answer(answer_id)
        self.object.user = self.request.user
        self.object.pub_date = timezone.now()
        self.object.save()
        self.get_success_url = reverse_lazy(
            'answer-detail', args=[str(question_id), str(answer_id)])
        return HttpResponseRedirect(self.get_success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer_id = self.kwargs['answer']
        answer = Answer.objects.get(pk=answer_id)
        context['answer'] = str(answer)
        return context
