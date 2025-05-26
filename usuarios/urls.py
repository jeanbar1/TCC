from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('escolher-tipo/', views.escolher_tipo, name='escolher_tipo'),
    # Usuários
    path('addUser/', views.addUser, name='addUser'),
    path('editUser/<int:id>/', views.editUser, name='editUser'),
    path('deleteUser/<int:id>/', views.deleteUser, name='deleteUser'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('listUser/', views.listUser, name='listUser'),
]