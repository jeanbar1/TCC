from django.urls import path
from . import views

urlpatterns = [
    path('listServico/', views.listServico, name="listServico"),
    path('listServico/<int:id>/', views.listServico, name="listServico"),
    path('addServico/', views.addServico, name="addServico"),
    path('editServico/<int:id>/', views.editServico, name="editServico"),
    path('deleteServico/<int:id>/', views.deleteServico, name="deleteServico"),
    
]