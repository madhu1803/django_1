from django import forms
from .models import Post
from django.contrib.auth.models import User

# POST CREATE/UPDATE FORM
class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "photo", "author", "content", "status"]


class LoginForm(forms.Form):

    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
