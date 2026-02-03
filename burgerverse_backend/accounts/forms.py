from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Signup form for custom User model.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
