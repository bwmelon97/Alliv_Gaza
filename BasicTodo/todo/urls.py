from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('change_complete/<int:pk>', views.change_todo_complete, name='change_complete'),
    path('delete/<int:pk>', views.delete, name='delete'),
]