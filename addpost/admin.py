from django.contrib import admin
from .models import AddPost
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


@admin.register(AddPost)
class AddPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

