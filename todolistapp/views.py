from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, reverse

my_todo = {
    'one': {"name": "breakfast", 'Priority': 1, 'finished': True,
            'description': 'hello from task number one this is hegabovic'},
    'two': {"name": "lunch", 'Priority': 1, 'finished': False,
            'description': 'hello from task number one this is hegabovic'},
    'three': {"name": "Dinner", 'Priority': 1, 'finished': False,
              'description': 'hello from task number one this is hegabovic'},
}


# Create your views here.

def todo_home(request):
    return HttpResponse('HELLO FROM THE FOKING DJANGO')


def todo_error(request):
    return HttpResponse('this is an error page')


# to return data in url as a dictionary use **kwargs

def todo_items(request, **kwargs):
    mytodo_key = kwargs.get('mytodo')
    mytodo_value = my_todo.get(mytodo_key)
    print('mytodo_value', mytodo_value)
    return HttpResponse(f"this is todo_items : {mytodo_value}")


def todo_array(request):
    return JsonResponse(my_todo)


def todo_home_template(request):
    return render(request, 'todolistapp/todo.html', context={'my_todo': my_todo})


def todo_details(request, **kwargs):
    mytodo_key = kwargs.get('mytodo')
    mytodo_value = my_todo.get(mytodo_key)
    return render(request, 'todolistapp/todo_details.html', context={'my_details': mytodo_value})


def todo_delete(request, **kwargs):
    mytodo_key = kwargs.get('mytodo')
    mytodo_value = my_todo.pop(mytodo_key)
    return redirect(reverse('todo:template'))


def todo_done(request, **kwargs):
    mytodo_key = kwargs.get('mytodo')
    mytodo_value = my_todo.get(mytodo_key)
    mytodo_value["finished"] = True
    return redirect(reverse('todo:template'))
