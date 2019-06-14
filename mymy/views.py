from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone


from .models import Post
from .forms import PostForm
from . import upbit_ticker
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect


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

def coin_ticker(request):
    if request.is_ajax():
        coin_name = request.POST.get('coin_name',None)
        data = upbit_ticker.dict_date(coin_name)
        dict = json.dumps(data)
        return HttpResponse(dict, content_type="application/json")
    else:
        coin_name = 'KRW-BTC'
        data = upbit_ticker.dict_date(coin_name)
        price = upbit_ticker.ticker()
        dict = json.dumps(data)
        return render(request, 'mymy/coin_ticker.html', {'prices' : price, 'data' : dict})

