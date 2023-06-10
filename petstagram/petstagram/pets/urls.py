from django.urls import path, include

from petstagram.pets.views import pet_add, pet_details, pet_edit, pet_delete

urlpatterns = [
    path('add/', pet_add, name='add pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', pet_details, name='pet details'),
        path('edit/', pet_edit, name='edit pet'),
        path('delete/', pet_delete, name='delete pet'),
    ]))
]