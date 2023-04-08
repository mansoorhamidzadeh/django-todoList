from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.todoListApiView,name='todoListApiView'),
    path('detail/<int:pk>/',views.todoListDetailApiView,name="todoListDetailApiView"),
    path('create/',views.todoListCreateApiView,name='todoListCreateApiView'),
    path('update/<int:pk>/',views.todoListUpdateApiView,name='todoListUpdateApiView'),
    path('delete/<int:pk>/',views.todoListDeleteApiView,name='todoListDeleteApiView'),
    path('users',views.userList),
]