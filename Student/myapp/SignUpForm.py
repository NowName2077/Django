from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction

from .models import UserProfile
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            UserProfile.objects.get_or_create(user=user)

        return user