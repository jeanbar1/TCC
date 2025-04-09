from django.urls import path
from . import views



urlpatterns = [
    path('addUser/', views.addUser, name="addUser"),
    path('editUser/<int:id>/', views.editUser, name="editUser"),
    path('deleteUser/<int:id>/', views.deleteUser, name="deleteUser"),
    path('profile/', views.profile, name="perfil"),
    path('profile<int:id>', views.profile, name="perfilUser"),
    path('<int:id>/muda_tipo/', views.muda_tipo, name="muda_tipo"),
    path('listUser/', views.listUser, name="listUser"),
]
