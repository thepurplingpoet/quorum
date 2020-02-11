from knowledge.models.question import Question
from django.views import generic


class QuestionDetail(generic.DetailView):
    model = Question
