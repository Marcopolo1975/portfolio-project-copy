from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class AddPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class AddPostRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"AddPost Request from {self.name}"