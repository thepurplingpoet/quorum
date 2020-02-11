from django.views.generic.edit import CreateView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from knowledge.models.question import Question
from django.http import HttpResponseRedirect


class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.pub_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
