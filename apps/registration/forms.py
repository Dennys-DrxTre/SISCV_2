from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserWhitEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text= "Requerido, 254 caracteres como maximo y debe ser valido.")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "is_staff")

        labels = {
            'is_staff': '¿Administrador?',
            'first_name': 'Nombres',
            'username': 'Usuario (Requerido para entrar al Sistema)'
        }
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email = email ).exists():
            raise forms.ValidationError("El Email ya esta registrado, prueba con otro")
        return email

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text= "Requerido, 254 caracteres como maximo y debe ser valido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email = email ).exists():
                raise forms.ValidationError("El Email ya esta registrado, prueba con otro")
        return email