from .models import AddPostRequest
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = AddPostRequest
        fields = ('name', 'email', 'message')