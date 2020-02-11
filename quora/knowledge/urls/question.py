from django.urls import path
from knowledge.views.question import list_all, detail, create, delete, update, vote


urlpatterns = [
    path('questions/', list_all.QuestionList.as_view(), name='questions'),
    path('question/<int:pk>', detail.QuestionDetail.as_view(),
         name='question-detail'),
    path('question/<int:pk>/', vote.question_vote, name='question_vote'),
    path('question/create/', create.QuestionCreate.as_view(), name='question_create'),
    path('question/<int:pk>/update/',
         update.QuestionUpdate.as_view(), name='question_update'),
    path('question/<int:pk>/delete/',
         delete.QuestionDelete.as_view(), name='question_delete'),

]
