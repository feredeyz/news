from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=3, label='', widget=forms.TextInput(attrs={"placeholder": "Имя пользователя", "id": "username"}))
    password = forms.CharField(max_length=30, min_length=3, label='', widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "id": "password"}))

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=3, label='', widget=forms.TextInput(attrs={"placeholder": "Имя пользователя", "id": "username"}))
    password = forms.CharField(max_length=30, min_length=3, label='', widget=forms.PasswordInput(attrs={"placeholder": "Пароль", "id": "password"}))
    confirm_password = forms.CharField(max_length=30, min_length=3, label='', widget=forms.PasswordInput(attrs={"placeholder": "Подтвердите пароль", "id": "confirm_password"}))

class AddNewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Заголовок', "id": 'title'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Новость", 'id': 'content'}))

class SearchNewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={"placeholder": "Заголовок новости", "id": "title"}))