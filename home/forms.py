# language_app/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
# language_app/forms.py
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # You can customize the form if needed (e.g., add extra fields, widgets, etc.)
    class Meta:
        model = User  # Assuming User model is imported
        fields = ['username', 'password']
