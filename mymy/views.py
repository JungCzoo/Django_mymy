from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Search
from .forms import PostForm, SearchForm
from django.shortcuts import redirect
from . import find_profile


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'mymy/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mymy/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mymy/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'mymy/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'mymy/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



def lol_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            summoner = form.save(commit=False)
            find = find_profile
            profiles = find.search(summoner)
            return render(request, 'mymy/lol_profile.html', {'profiles' : profiles})
    else:
        form = SearchForm()
        return render(request, 'mymy/lol_search.html', {'form' : form})

def lol_profile(request):
    return render(request, 'mymy/lol_profile.html')