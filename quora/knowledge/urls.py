from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('questions/', views.QuestionList.as_view(), name='questions'),
    path('users/', views.UserList.as_view(), name='users'),
    path('question/<int:pk>', views.QuestionDetail.as_view(), name='question-detail'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user-detail'),

]