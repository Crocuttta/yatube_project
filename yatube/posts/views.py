from django.shortcuts import get_object_or_404, render, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Group, Post
from .constans import NUMBER_OF_POSTS_PER_PAGE
from .forms import PostForm

User = get_user_model()

def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10) 
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)    
    posts = group.posts.all()[:NUMBER_OF_POSTS_PER_PAGE]
   
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, id=post_id)
    posts_count = Post.objects.filter(author=post.author).count()   
    
    template = 'posts/post_detail.html'
    context = {
        'post' : post, 
        'posts_count' : posts_count
    }
    return render(request, template, context) 


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author)
    paginator = Paginator(post_list, settings.NUMBER_OF_POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'
    context = {'page_obj': page_obj, 'author': author}
    return render(request, template, context) 


def post_create(request):
    if request.method == 'POST':        
        form = PostForm(request.POST)       
        if form.is_valid():
            post = form.save(False)
            post.author = request.user
            post.save()            
            return redirect('posts:profile', post.author)
        else:
            return render(request, 'posts/post_create.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'posts/post_create.html', {'form': form})

@login_required   
def post_edit(request, post_id):    
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post_id=post.id)
    context = {'form': form, 'is_edit': True}
    return render(request, 'posts/post_create.html', context)