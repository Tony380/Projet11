from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.LoginFormView.as_view(
        template_name='login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile, name='profile'),
    path('update', views.update, name='update'),
    path('username', views.modify_username, name='username'),

]

app_name = 'users'
