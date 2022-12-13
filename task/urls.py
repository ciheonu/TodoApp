from django.urls import path
from . import views


urlpatterns = [
    path('', views.lists, name="list"),
    path('delete_all/', views.delete_all, name="delete_all"),
    path('delete_completed', views.delete_complete, name="delete_completed"),
    path('delete_task/<int:pk>', views.delete_task, name="delete_task"),
    path('edit_task/<int:pk>', views.edit_task, name="edit_task"),
]
