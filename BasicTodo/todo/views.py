"""
인덱스 템플릿을 render하는  index
새로운 Todo를 생성하는      create
Todo의 내용을 수정하는      update 
Todo의 완료여부를 수정하는   change_todo_complete
Todo를 삭제하는           delete

함수들이 있습니다.

todo.models의 TodoList 모델과 django auth의 User 모델을 사용합니다.
"""


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from rest_framework import generics

from .models import TodoList
from .serializers import TodoListSerializer

def index(request):
    '''
    index 템플릿을 render하는 함수입니다.

    get_user를 통해 로그인 정보를 확인하여, 
    로그인한 유저가 없으면, index_not_login 템플릿을 render하고,
    로그인한 유저가 있으면, 해당 유저의 todolist를 최근 수정된 기준으로 정렬해 context로 만들고,
    이를 index_login 템플릿과 함께 render합니다.
    '''
    user = auth.get_user(request)
    if not user.is_authenticated:
        return render(request, 'todo/index_not_login.html')
    
    latest_todolist = user.todolist_set.order_by('-last_mod')
    context = {
        'latest_todolist' : latest_todolist
    }
    return render(request, 'todo/index_login.html', context)


def create(request):
    '''
    로그인된 유저의 todolist를 새로운 레코드를 생성하는 함수입니다.

    POST로 받은 request에 한해서 생성을 하며,
    함수를 redirect('base')를 리턴하여, index 함수가 호출되게 합니다.
    '''
    if request.method == 'POST':
        user = auth.get_user(request)
        user.todolist_set.create(
            todo_content=request.POST['new_todo'],
            pub_date=timezone.now(),
            last_mod=timezone.now()
        )
        return redirect('base')

    return redirect('base')


def update(request, pk):
    '''
    url을 통해 받은 pk값을 가진 todolist를 받아와 인스턴스를 생성하고,
    해당 인스턴스를 modify_content 메서드를 실행해 Todo 내용과 last_mod값을 바꾸고
    .save()를 통해 인스턴스 값을 DB 서버에 저장합니다.

    POST로 받은 request에 한해서 해당 내용을 실행하며,
    함수를 redirect('base')를 리턴하여, index 함수가 호출되게 합니다.

    [update] 다른 유저의 todolist를 변경할 수 없도록 검증하는 코드가 추가되었습니다.
    '''
    if request.method == "POST":
        user = auth.get_user(request)
        todolist = get_object_or_404(TodoList, pk=pk)

        # todolist 소유자와 user가 일치하지 않는 경우, 
        # 추가 작업 없이 홈 화면으로 이동
        if todolist.owner != user:
            return redirect('base')

        todolist.modify_content(request.POST['modified_content'])
        todolist.save()
        return redirect('base')

    return redirect('base')

def change_todo_complete(request, pk):
    '''
    해당 todolist의 완료여부 값을 변경합니다.
    함수의 작동 방식은 update와 동일합니다.
    '''
    if request.method == "POST":
        user = auth.get_user(request)
        todolist = get_object_or_404(TodoList, pk=pk)

        # todolist 소유자와 user가 일치하지 않는 경우, 
        # 추가 작업 없이 홈 화면으로 이동
        if todolist.owner != user:
            return redirect('base')

        todolist.change_complete()
        todolist.save()
        return redirect('base')

    return redirect('base')


def delete(request, pk):
    '''
    해당 todolist를 삭제합니다.
    함수의 작동 방식은 update와 동일합니다.
    '''
    if request.method == "POST":
        user = auth.get_user(request)
        todolist = get_object_or_404(TodoList, pk=pk)

        # todolist 소유자와 user가 일치하지 않는 경우, 
        # 추가 작업 없이 홈 화면으로 이동
        if todolist.owner != user:
            return redirect('base')

        todolist.delete()
        return redirect('base')

    return redirect('base')


class ListTodo(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer