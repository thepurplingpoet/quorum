from django.db import models
from django.urls import reverse
from users.models import User

from knowledge.models.question import Question
from knowledge.models.answer import Answer

class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(verbose_name="")
    pub_date = models.DateField('date added')
    updated = models.DateField(verbose_name='date published', blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=True, default=0)
    downvotes = models.IntegerField(blank=True, null=True, default=0)  
    upvote_users = models.ManyToManyField(User, related_name='Users_who_upvoted_this_comment')
    downvote_users = models.ManyToManyField(User, related_name='Users_who_downvoted_this_comment')
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.user.username}\'s answer to {self.answer.question.question_text[:20]} ...'

    class Meta: 
        ordering = ['-pub_date']


