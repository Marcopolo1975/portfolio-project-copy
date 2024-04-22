from django.shortcuts import render
from django.contrib import messages
from .models import AddPost
from .forms import AddPostForm


def addpost(request):
    
    if request.method == "POST":
        addpost_form = AddPostForm(data=request.POST)
        if addpost_form.is_valid():
            addpost_form.save()
            messages.add_newpost(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")
    addpost = AddPost.objects.all().order_by('-updated_on').first()
    addpost_form = AddPostForm()

    return render(
        request,
        "addpost/addpost.html",
        {
            "addpost": addpost,
            "addpost_form": addpost_form
        },
    )