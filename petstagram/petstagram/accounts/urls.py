from django.urls import path, include

from petstagram.accounts.views import login_user, register_user, details_user, delete_user, edit_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('register/', register_user, name='register user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='details user'),
        path('delete/', delete_user, name='delete user'),
        path('edit/', edit_user, name='edit user'),
    ]))
]