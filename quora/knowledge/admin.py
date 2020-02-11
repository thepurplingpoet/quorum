from django.contrib import admin

from knowledge.models.question import Question
from knowledge.models.answer import Answer
from knowledge.models.comment import Comment

from users.models import User
# Register your models here.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)

