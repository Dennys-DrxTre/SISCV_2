from .forms import UserWhitEmail, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.

class SignupView(SuccessMessageMixin, CreateView):
    form_class = UserWhitEmail
    template_name = 'registration/signup.html'
    success_message = "Empleado Registrado Exitosamente"
    success_url = reverse_lazy('inicio:list_emp')

    def get_form(self, form_class=None):
        form = super(SignupView, self).get_form()

        #Modificar en tiempo real
        form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombres'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Apellidos'})
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Correo Electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repetir la contraseña'})
        form.fields['is_staff'].widget = forms.CheckboxInput()
        return form

class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url= reverse_lazy('perfil')
    template_name = 'registration/profile_update_form.html'

    def get_object(self):
        # recuperar el objeto que se va a editar
        return self.request.user
    
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form