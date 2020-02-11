from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User

class UserUpdate(LoginRequiredMixin, UpdateView):
    model=User
    fields=['firstname', 'lastname', 'bio']