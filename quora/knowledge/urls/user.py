from django.urls import path
from knowledge.views import user
from knowledge.views.user import list_all, detail, update

urlpatterns = [
   
    path('users/', user.list_all.UserList.as_view(), name='users'),
    path('user/<int:pk>', user.detail.UserDetail.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', user.update.UserUpdate.as_view(), name='user_update'),
]
