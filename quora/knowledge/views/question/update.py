from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from knowledge.models.question import Question
from users.models import User
from django.http import HttpResponseRedirect

class QuestionUpdate(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['question_text']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.updated = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())