from django.urls import path
from knowledge.views import answer
from knowledge.views.answer import detail, create, delete, update, vote


urlpatterns = [
    path('question/<int:question>/answer/<int:pk>',
         answer.detail.AnswerDetail.as_view(), name='answer-detail'),
    path('question/<int:question>/answer/<int:pk>/',
         answer.vote.answer_vote, name='answer_vote'),
    path('question/<int:question>/answer/create/',
         answer.create.AnswerCreate.as_view(), name='answer_create'),
    path('question/<int:question>/answer/<int:pk>/update/',
         answer.update.AnswerUpdate.as_view(), name='answer_update'),
    path('question/<int:question>/answer/<int:pk>/delete/',
         answer.delete.AnswerDelete.as_view(), name='answer_delete'),
]
