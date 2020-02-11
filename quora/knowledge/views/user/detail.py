from django.views import generic
from users.models import User
from knowledge.models.question import Question

class UserDetail(generic.DetailView):
    model = User
    context_object_name = "question_poster"
