from django.urls import path
from . import views

# 유저에게 보여 줄 화면과 처리하는 함수를 연결에 사용

urlpatterns = [
	path('', views.index, name='index'),
	path('createTodo/', views.createTodo, name='createTodo'),
	path('doneTodo/', views.doneTodo, name='doneTodo')
]
