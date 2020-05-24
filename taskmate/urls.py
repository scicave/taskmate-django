"""taskmate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist_app import views
from users import views as views_2
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('todolist',views.todolist,name='todolist'),
    path("",views.index,name='index'),
    path('delete/<task_id>/',views.delete_task,name='delete_task'),
    path('pending/<task_id>/',views.pending_task,name='pending_task'),
    path('edit/<task_id>/',views.edit,name='edit_task'),
    path('admin/', admin.site.urls),
    path('complete/<task_id>/',views.complete_task,name='complete_task'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('account/register',views_2.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    
]