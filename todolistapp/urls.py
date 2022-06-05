from todolistapp.views import todo_home, todo_error, todo_items, todo_array, todo_home_template, todo_details,todo_done,todo_delete
from django.urls import path

app_name = 'todo'
urlpatterns = [

    path('home', todo_home, name='home'),
    path('home/template', todo_home_template, name='template'),
    path('home/template/todo_details/<str:mytodo>', todo_details, name='todo_details'),
    path('home/template/done/<str:mytodo>', todo_done, name='todo_done'),
    path('home/template/delete/<str:mytodo>', todo_delete, name='todo_delete'),

    path('todos', todo_array),
    # send query parameters
    path('items/<str:mytodo>', todo_items),

    path('error', todo_error),

]
