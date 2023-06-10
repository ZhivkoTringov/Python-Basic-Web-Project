from django.urls import path, include

from petstagram.photos.views import photo_add, photo_edit, photo_details

urlpatterns = [
    path('add/', photo_add, name='add photo'),
    path('<int:pk>/', include([
        path('edit/', photo_edit, name='edit photo'),
        path('', photo_details, name='details photo'),
    ]))
]