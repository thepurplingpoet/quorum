from django import forms
from django import ModelForm 
from knowledge.models import Answer, User, Question, Comment

class editAnswer(ModelForm):
    class Meta:
        mode=Answer
        fields=['answer_text']


class editProfile(ModelForm):
    class Meta:
        mode=User
        fields=['name','bio']
