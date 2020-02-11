from django.shortcuts import get_object_or_404, redirect
from knowledge.models.question import Question
from knowledge.views.utils import vote


def question_vote(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if request.method == 'POST':
        user = request.user
        vote(question, request.POST, user)

    return redirect('question-detail', pk)
