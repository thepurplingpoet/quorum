from django.urls import path
from knowledge.views import index

urlpatterns = [
    path('', index.index, name='index'),
]
