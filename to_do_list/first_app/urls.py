from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks, name='show'),
    path('add/', views.add_task, name='add'),
    path('completed_list/', views.completed_task_list, name='completed_list'),
    path('edit/<int:id>', views.edit_task, name="edit"),
    path('delete/<int:id>', views.delete_task, name="delete"),
    path('completed/<int:id>', views.complete_task, name="complete"),
]
