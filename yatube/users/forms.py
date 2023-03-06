from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import get_user_model
from .models import Contact

User = get_user_model()

class ContactForm(forms.ModelForm):
    class Meta:       
        model = Contact      
        fields = ('name', 'email', 'subject', 'body') 



#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('first_name', 'last_name', 'username', 'email')


#форма смены пароля
#class PasswChangeForm(PasswordChangeForm):    
#    model = User
#    field_order = ('old_password', 'new_password1', 'new_password2')

#форма сброса пароля
'''
class PasswResetForm(PasswordChangeForm):
    model = User
    field_order = ('new_password1', 'new_password2')
'''
#форма смены пароля по ссылке из письма 
class PasswSetPasswordForm(SetPasswordForm):
    model = User
