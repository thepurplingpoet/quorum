from django.db import models
from django.urls import reverse
from users.models import User
from knowledge.models.question import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField(verbose_name="")
    upvotes = models.IntegerField(blank=True, null=True, default=0)
    downvotes = models.IntegerField(blank=True, null=True, default=0)    
    pub_date = models.DateField('date added')
    updated = models.DateField(verbose_name='date published', blank=True, null=True)
    upvote_users = models.ManyToManyField(User, related_name='Users_who_upvoted_this_answer')
    downvote_users = models.ManyToManyField(User, related_name='Users_who_downvoted_this_answer')

    def __str__(self):
        return f'{self.user.username}\'s answer to {self.question.question_text[:20]} ...'

    class Meta: 
        ordering = ['-pub_date', 'upvotes']

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)]) 

    def get_answer_short(self):
        return self.answer_text[:50]
