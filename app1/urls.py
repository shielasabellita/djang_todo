from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.logout, name="logout"),
    path('getlist', views.getlist, name="getlist"),
    path('view', views.view_details, name="details"),
    path('addTodo', views.add_todo, name="add_todo"),
    path('edit', views.edit_todo, name="edit_todo"),
    # path('delete/<str:id>/', views.delete_todo, name="delete_todo"),
    path('delete', views.delete_todo, name="delete_todo"),
    
]