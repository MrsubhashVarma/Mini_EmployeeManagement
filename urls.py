from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.employee_login, name='employee_login'),
    path('logout/', views.employee_logout, name='employee_logout'),
    path('dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('', views.view_all_employees, name='view_all_employees'),
    path('add/', views.add_employee, name='add_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
]
