from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.LoginView),
    path('register/',views.registerView),
    path('todoList/',views.todoList,name='todoList'),
    path('todoList/<int:pk>/',views.todoListDetail,name='todoList-detail'),
    path('todoList/create/',views.todoListCreate,name='todoList-create'),
    path('todoList/update/<int:pk>/',views.todoListUpdate,name='todoList-update'),
    path('todoList/delete/<int:pk>/',views.todoListDelete,name='todoList-delete'),
]