from django.shortcuts import render
from knowledge.models.question import Question


def index(request):
    """View function for home page of site."""

    latest_questions = Question.objects.all()[:5]

    context = {
        'questions': latest_questions
    }

    return render(request, 'index.html', context=context)
