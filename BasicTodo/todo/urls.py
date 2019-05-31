'''
index url은 클라이언트에게 보여지는 템플릿을 render하는 url이고,
다른 4개는 POST로 요청받은 정보를 바탕으로 백앤드 작업을 수행하는 url입니다.
update, change, delete는 특정 인스턴스(레코드)에 적용하는 함수이므로 url에 /<ink:pk>를 통해 해당 인스턴스(레코드)의 pk값을 활용합니다.
'''

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