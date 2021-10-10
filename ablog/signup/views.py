from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm,EditProfile,PasswordsChangingForm
from django.contrib.auth.views import PasswordChangeView


class PasswordsChangeView(PasswordChangeView):
    
    #form_class = PasswordChangeForm
    form_class = PasswordsChangingForm
    template_name = 'registration/edit_password.html'
    success_url = reverse_lazy('success')

def password_success(request):
    return render(request, 'registration/success.html',{})

class UserRegisterView(generic.CreateView):
    
    #form_class = UserCreationForm earlieer was this 
    form_class = SignupForm # now this is new our own custom form 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfile
    #form_class = UserCreationForm
    template_name = 'registration/edit_registration.html'
    success_url = reverse_lazy('home')
 
    def get_object(self):    #this is some predefined function which we are overriding so can't change the func name here
        return self.request.user


