from django.shortcuts import get_object_or_404, redirect
from knowledge.models.comment import Comment
from knowledge.views.utils import vote


def comment_vote(request, question, answer, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        user = request.user
        vote(comment, request.POST, user)

    return redirect('answer-detail', question, answer)
