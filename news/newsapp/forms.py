from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=3)
    password = forms.CharField(max_length=30, min_length=3, widget=forms.PasswordInput())

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=3)
    password = forms.CharField(max_length=30, min_length=3, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, min_length=3, widget=forms.PasswordInput())

class AddNewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Заголовок'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Новость"}))

class SearchNewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={"placeholder": "Заголовок новости"}))