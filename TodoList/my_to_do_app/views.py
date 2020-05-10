from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
    # HTML을 User에게 보여줄 때, render() 함수 사용
	# request에 user, session과 같은 중요 값 전달
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    # models.py의 Todo 모델(테이블)로 새 데이터 생성 
    new_todo = Todo(content = user_input_str)
    # DB에 저장
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("id:", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))

