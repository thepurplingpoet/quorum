from users.models import User
from django.views import generic

class UserList(generic.ListView):
    model = User