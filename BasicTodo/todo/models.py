"""
django Model의 서브 클래스인 TodoList가 정의되어 있습니다. 
"""

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoList(models.Model):
    '''
    TodoList의 데이터를 가진 필드들과 메서드가 정의되어 있으며, DB의 todo_todolist 테이블과 연결되어 있습니다.

    [Fields Description]
    owner: auth_user 테이블과 ManyToOne 관계를 가지고 있으며, 소유자의 id를 저장합니다.
    todo_content: Todo 내용을 담는 CharFiled입니다.
    is_completed: Todo의 완료 여부 정보를 담는 BooleanField입니다.
    pub_date: Todo가 생성된 날짜, 시간 정보를 담는 DateTimeFiled입니다.
    last_mod: Todo가 마지막으로 수정된 날짜, 시간 정보를 담는 DateTimeFiled입니다.
    
    [Method Description]
    modify_content: 새로운 string을 받아 인스턴스의 todo_content를 수정합니다.
    change_complete: 인스턴스의 is_completed 값을 바꿉니다.
    '''
    # Fields
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_content = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    last_mod = models.DateTimeField('lastest modified date time')

    # Methods
    def __str__(self):
        return self.todo_content

    def modify_content(self, newStr):
        '''
        새로운 string을 받아 인스턴스의 todo_content를 수정합니다.
        last_mod 값을 함수가 실행된 시간으로 설정합니다.
        
        [updated] 아무 문자 입력 없을 때는 수정되지 않습니다.
        '''
        if not newStr:
            return

        self.todo_content = newStr
        self.last_mod = timezone.now()

    def change_complete(self):
        '''
        인스턴스의 is_completed 값을 바꿉니다.
        last_mod 값을 함수가 실행된 시간으로 설정합니다.
        '''
        if self.is_completed:
            self.is_completed = False
        else:
            self.is_completed = True
        self.last_mod = timezone.now()

