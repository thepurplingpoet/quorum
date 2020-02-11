from django.shortcuts import get_object_or_404, redirect
from knowledge.models.answer import Answer
from knowledge.views.utils import vote

def answer_vote(request, question, pk):
    answer = get_object_or_404(Answer, pk=pk)

    if request.method == 'POST':
        user = request.user
        vote(answer, request.POST, user)

    return redirect('answer-detail', question , pk)
