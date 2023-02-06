from django.shortcuts import render
#from django.http import HttpResponse 

def index(request): 
    template = 'posts/index.html'

    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Это главная страница проекта Yatube',
    }

    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Это не главная страница проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)
    
