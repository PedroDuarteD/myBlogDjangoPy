from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('thoughts',views.thoughts, name="thoughts"),
    path('users',views.getUsers, name="users"),
    path('addUser',views.setUser, name="adduser"),
    path('addThought',views.setThought, name="addthought"),
    
]