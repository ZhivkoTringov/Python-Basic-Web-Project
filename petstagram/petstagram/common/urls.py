from django.http import request
from django.urls import path

from petstagram.common.views import index

urlpatterns = [
    path('', index, name='index')
]