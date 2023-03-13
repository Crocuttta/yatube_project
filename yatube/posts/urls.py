from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # Профайл пользователя
    path('profile/<str:username>/', views.profile, name='profile'),    
    # Редактирование записи
    path('posts/<post_id>/edit/', views.post_edit, name='post_edit'),
    # Просмотр записи
    path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),    
]
