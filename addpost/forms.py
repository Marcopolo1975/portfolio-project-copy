from .models import AddPost
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = AddPost
        fields = ('title','title_image','content')