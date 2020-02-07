from django import forms
from django.forms import ModelForm
from knowledge.models import Answer, User, Question, Comment

class editAnswer(ModelForm):
    class Meta:
        model=Answer
        fields=['answer_text']


class editProfile(ModelForm):
    class Meta:
        model=User
        fields=['name','bio']

class CreateQuestion(ModelForm):
    class Meta:
        model=Question
        fields=['question_text']

