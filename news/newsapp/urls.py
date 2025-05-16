from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('add', add, name='add'),
    path('search', search, name='search')
]