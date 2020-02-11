from django.urls import path
from knowledge.views import index, question, answer, comment, user
from knowledge.views.question import list_all, detail, create, delete, update, vote
from knowledge.views.answer import  detail, create, delete, update, vote
from knowledge.views.comment import create, delete, update, vote
from knowledge.views.user import list_all, detail, update

urlpatterns = [
    path('', index.index, name='index'),
    path('questions/', question.list_all.QuestionList.as_view(), name='questions'),
    path('users/', user.list_all.UserList.as_view(), name='users'),
    path('question/<int:pk>', question.detail.QuestionDetail.as_view(), name='question-detail'),
    path('user/<int:pk>', user.detail.UserDetail.as_view(), name='user-detail'),
    path('question/<int:question>/answer/<int:pk>', answer.detail.AnswerDetail.as_view(), name = 'answer-detail'),
    path('question/<int:pk>/', question.vote.question_vote, name='question_vote'),
    path('question/<int:question>/answer/<int:pk>/', answer.vote.answer_vote, name='answer_vote'),
    path('question/<int:question>/answer/<int:answer>/comment/<int:pk>/', comment.vote.comment_vote, name='comment_vote'),

]

urlpatterns += [  
    path('question/<int:question>/answer/create/', answer.create.AnswerCreate.as_view(), name='answer_create'),
    path('question/<int:question>/answer/<int:pk>/update/', answer.update.AnswerUpdate.as_view(), name='answer_update'),
    path('question/<int:question>/answer/<int:pk>/delete/', answer.delete.AnswerDelete.as_view(), name='answer_delete'),
]

urlpatterns += [  
    path('user/<int:pk>/update/', user.update.UserUpdate.as_view(), name='user_update'),
]

urlpatterns += [  
    path('question/create/', question.create.QuestionCreate.as_view(), name='question_create'),
    path('question/<int:pk>/update/', question.update.QuestionUpdate.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', question.delete.QuestionDelete.as_view(), name='question_delete'),
]

urlpatterns += [  
    path('question/<int:question>/answer/<int:answer>/comment/create/', comment.create.CommentCreate.as_view(), name='comment_create'),
    path('question/<int:question>/answer/<int:answer>/comment/<int:pk>/update/', comment.update.CommentUpdate.as_view(), name='comment_update'),
    path('question/<int:question>/answer/<int:answer>/comment/<int:pk>/delete/', comment.delete.CommentDelete.as_view(), name='comment_delete'),
]