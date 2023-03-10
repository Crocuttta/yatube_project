from django.shortcuts import render

# users/views.py
# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView, UpdateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm#, PasswChangeForm #PasswResetForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

#смена пароля авторизованным пользователем
#class ChangePassword(UpdateView):
 #   form_class = PasswChangeForm
    # После успешного изменения пароля перенаправляем пользователя.
 #   success_url = reverse_lazy('users:password_change/done/')
 #   template_name = 'users/password_change_form.html'


'''
class ResetPassword(UpdateView):
    form_class = PasswResetForm
    # После успешной регистрации перенаправляем пользователя.
    success_url = reverse_lazy('users:password_reset/done/')
    #template_name = 'users/password_reset_confirm.html'
    template_name = 'users/password_reset.html'
'''