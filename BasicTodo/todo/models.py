import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_content = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published')
    last_mod = models.DateTimeField('lastest modified date time')

    def __str__(self):
        return self.todo_content

    def modify_content(self, newStr):
        self.todo_content = newStr
        self.last_mod = timezone.now()

    def change_complete(self):
        if self.is_completed:
            self.is_completed = False
        else:
            self.is_completed = True
        self.last_mod = timezone.now()

