from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.QuestionList.as_view(), name='questions'),
    path('users/', views.UserList.as_view(), name='users'),
    path('question/<int:pk>', views.QuestionDetail.as_view(), name='question-detail'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user-detail'),

]

urlpatterns += [  
    path('answer/create/', views.AnswerCreate.as_view(), name='answer_create'),
    path('answer/<int:pk>/update/', views.AnswerUpdate.as_view(), name='answer_update'),
    path('answer/<int:pk>/delete/', views.AnswerDelete.as_view(), name='answer_delete'),
]

urlpatterns += [  
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
]

urlpatterns += [  
    path('question/create/', views.QuestionCreate.as_view(), name='question_create'),
    path('question/<int:pk>/update/', views.QuestionUpdate.as_view(), name='question_update'),
    path('question/<int:pk>/delete/', views.QuestionDelete.as_view(), name='question_delete'),
]

urlpatterns += [  
    path('comment/create/', views.CommentCreate.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
]