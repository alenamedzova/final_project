from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, get_user_model


# Create your views here.
class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class SignUpView(generic.CreateView):
    # pripojíme formulár
    form_class = SignUpForm  # použijeme formulár definovaný vyššie
    success_url = reverse_lazy('login')  # kam nás to presmeruje, v prípade úspechu
    template_name = 'accounts/signup.html'  # použijeme tento template
