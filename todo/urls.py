from django.urls import path
from . import views

urlpatterns = [
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
