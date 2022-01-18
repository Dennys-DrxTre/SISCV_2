from django.urls import path
from .views import SignupView, EmailUpdate

urlpatterns = [

    path('signup/', SignupView.as_view(), name="signup" ),
    path('perfil/email/', EmailUpdate.as_view(), name='perfil_email' ),


]