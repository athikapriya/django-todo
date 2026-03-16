from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_list, name='api_tasks_list'),
    path('tasks/<int:pk>/', views.task_detail, name='api_task_detail'),
    path('tasks/completed/', views.completed_tasks, name='api_tasks_completed'),
]