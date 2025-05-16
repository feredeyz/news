from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm, AddNewsForm, SearchNewsForm # type: ignore
from .models import User, News
import bcrypt

# Страницы
def index(request):
    news = News.objects.all()
    return render(request, 'index.html', {"news": news})

def add(request):
    if request.method == "POST":
        form = AddNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            News.objects.create(title=title, content=content, source=request.session["username"])
            messages.success(request, "Новость успешно опубликована.")
            return redirect('home')
        else:
            messages.error("Форма не валидна.")
            return redirect('add')
    elif request.method == "GET":
        if not request.session["username"]:
            messages.error(request, "Сначала войдите в аккаунт.")
            return redirect('home')
        form = AddNewsForm()
        return render(request, "add.html", {"form": form})

def search(request):
    if request.method == "POST":
        form = SearchNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            results = News.objects.filter(title=title)
            return render(request, 'search.html', {"form": form, "results": results})
        else:
            messages.error(request, "Форма не валидна.")
    elif request.method == "GET":
        form = SearchNewsForm()
        return render(request, 'search.html', {"form": form})

# Аутентификация
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(username=username)
                if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                    messages.success(request, "Успешный вход.")
                    request.session["username"] = username
                    return redirect('home')
                else:
                    form = LoginForm()
                    return render(request, 'login.html', {"form": form, "error": "Неправильный пароль"})
            except User.DoesNotExist:
                form = LoginForm()
                return render(request, 'login.html', {"form": form, "error": "Пользователя с данным именем не существует"})
        else:
            messages.error(request, "Форма не валидна")
            return redirect('login')
    elif request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

def logout(request):
    request.session["username"] = None
    return redirect('home')

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.error(request, "Пароли не совпадают.")
                return redirect('signup')
            try:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                user = User.objects.create(username=username, password=hashed_password)
                request.session['username'] = username
                messages.success(request, "Вы успешно зарегистрировались")
                return redirect('home')
            except Exception as e:
                print(f"Error: {e}")
                messages.error(request, "Пользователь с таким именем уже существует.")
                return redirect('signup')
        else:
            messages.error(request, "Форма не валидна.")
            return redirect('signup')
    elif request.method == "GET":
        form = RegistrationForm()
        return render(request, 'signup.html', {"form": form})