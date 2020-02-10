from django.db import models
from django.urls import reverse
from users.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200,verbose_name= 'Question')
    pub_date = models.DateField(verbose_name='date published')
    updated = models.DateField(verbose_name='date published', blank=True, null=True)
    upvotes = models.IntegerField(blank=True, null=True, default=0)
    downvotes = models.IntegerField(blank=True, null=True, default=0)  
    upvote_users = models.ManyToManyField(User, related_name='Users_who_upvoted_this_question')
    downvote_users = models.ManyToManyField(User, related_name='Users_who_downvoted_this_question')
    
    def __str__(self):
        return self.question_text
    
    class Meta: 
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)]) 
    


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
        return f'Answer by {self.user.username} to {self.question.question_text[:20]} ...'

    class Meta: 
        ordering = ['-pub_date', 'answer_text']

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)]) 

    def get_answer_short(self):
        return self.answer_text[:50]

class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
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


