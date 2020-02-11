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
    