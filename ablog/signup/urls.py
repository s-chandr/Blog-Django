
from django.urls import path
from . import views
from .views import UserRegisterView,UserEditView,PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [

    path('register/',UserRegisterView.as_view(),name='register'),
    path('edit_progfile/',UserEditView.as_view(),name='update_profile'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration/edit_password.html'),name='update_password'),
    #instead this we create our own passwords change view here
    path('password/',PasswordsChangeView.as_view(template_name = 'registration/edit_password.html'),name='update_password'),
    path('pass_sucess/',views.password_success,name ='success'),
]
