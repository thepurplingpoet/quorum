from knowledge.models.question import Question
from django.views import generic


class QuestionList(generic.ListView):
    model = Question
