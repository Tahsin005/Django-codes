from django.shortcuts import render, redirect
from posts.forms import PostForm
from . import models
# Create your views here.
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('add_post')
    return render(request, 'add_post.html', {'form': form})


def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    return render(request, 'add_post.html', {'form': form})

def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('homepage')