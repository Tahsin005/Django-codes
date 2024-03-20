from django.shortcuts import render, redirect
from posts.forms import PostForm, CommentForm
from . import models
from posts.models import Post
from django.contrib.auth.decorators import login_required


from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data['author'] = request.user
            form.instance.author = request.user
            form.save()
            print(form.cleaned_data)
            return redirect('add_post')
    return render(request, 'add_post.html', {'form': form})

# Add post using class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk = id)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            print(form.cleaned_data)
            return redirect('homepage')
    return render(request, 'add_post.html', {'form': form})

# Edit post using class based view
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    

@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk = id)
    post.delete()
    return redirect('profile')

# Delete post using class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    
    
class DetailPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context