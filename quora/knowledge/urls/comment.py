from django.urls import path
from knowledge.views import comment
from knowledge.views.comment import create, delete, update, vote

urlpatterns = [
    path('question/<int:question>/answer/<int:answer>/comment/create/', comment.create.CommentCreate.as_view(), name='comment_create'),
    path('question/<int:question>/answer/<int:answer>/comment/<int:pk>/update/', comment.update.CommentUpdate.as_view(), name='comment_update'),
    path('question/<int:question>/answer/<int:answer>/comment/<int:pk>/delete/', comment.delete.CommentDelete.as_view(), name='comment_delete'),
    path('question/<int:question>/answer/<int:answer>/comment/<int:pk>/', comment.vote.comment_vote, name='comment_vote'),

]