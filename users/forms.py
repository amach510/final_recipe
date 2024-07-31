from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=120)
    pic = forms.ImageField(label='Profile Picture', required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ("username", "name", "pic", "bio", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # Customize help texts
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = "Your password must contain at least 8 characters and can't be entirely numeric."
        self.fields['pic'].required = True
        #self.fields['password2'].help_text = None