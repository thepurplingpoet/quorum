from knowledge.models.answer import Answer
from django.views import generic


class AnswerDetail(generic.DetailView):
    model = Answer