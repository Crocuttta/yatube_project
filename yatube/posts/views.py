from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from .models import Group, Post
from .constans import NUMBER_OF_POSTS_PER_PAGE

User = get_user_model()

def index(request):
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts,
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
    context = {
    }
    return render(request, 'posts/post_detail.html', context) 


def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    context = {username
    }
    return render(request, 'posts/profile.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author)
    paginator = Paginator(post_list, settings.NUMBER_OF_POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'
    context = {'page_obj': page_obj, 'author': author}
    return render(request, template, context)    