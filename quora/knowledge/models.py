from django.db import models
from django.urls import reverse
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=12)
    bio = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)]) 


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    upvotes = models.IntegerField(blank=True, null=True, default=0)
    downvotes = models.IntegerField(blank=True, null=True, default=0)  
    def __str__(self):
        return self.question_text
    
    class Meta: 
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)]) 


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField()
    upvotes = models.IntegerField(blank=True, null=True, default=0)
    downvotes = models.IntegerField(blank=True, null=True, default=0)    
    pub_date = models.DateField('date added')

    def __str__(self):
        return f'Answer by {self.user.username} to {self.question.question_text[:20]} ...'

    class Meta: 
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)]) 


class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateField('date added')
    upvotes = models.IntegerField(blank=True, null=True, default=0)
    downvotes = models.IntegerField(blank=True, null=True, default=0)  
    def __str__(self):
        return f'Comment by {self.user.name} on {self.user.username}\'s answer to {self.answer.question.question_text[:20]} ...'

    class Meta: 
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)]) 

