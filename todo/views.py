from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User
from models import Todo


def todolist(request):
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)

    return render(request, 'todo/simpleTodo.html', {'todolist': todolist,'finishtodos': finishtodos })
    # return render_to_response('todo/simpleTodo.html',{
    #                           'todolist': todolist, 'finishtodos': finishtodos },
    #                           RequestContext(request)
    #                           )

def todofinish(request,id=""):
    todo = Todo.objects.get(id=id)
    if todo.flag == "1":
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/todo/todolist')

    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response(
        'todo/simpleTodo.html',
        {'todolist':todolist,'finishtodos':finishtodos},
        RequestContext(request)
    )


def todoback(request,id=""):
    todo = Todo.objects.get(id=id)
    if todo.flag == "0":
        todo.flag = '1'
        todo.save()
        return HttpResponseRedirect('/todo/todolist')

    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response(
        'todo/simpleTodo.html',
        {'todolist': todolist, 'finishtodos': finishtodos},
        RequestContext(request)
    )

def tododelete(request,id=""):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        return Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/todo/todolist')
    todolist = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render_to_response(
        'todo/simpleTodo.html',
        {'todolist': todolist, 'finishtodos': finishtodos},
        RequestContext(request)
    )

def addtodo(request):
    if request.method == 'POST':
        atodo = request.POST.get('todo')
        priority = request.POST.get('priority')
        user = User.objects.get(id='1')
        todo = Todo(user=user,todo=atodo,priority=priority,flag='1')
        todo.save()
        return HttpResponseRedirect('/todo/todolist')
    else:
        return render_to_response(
            'todo/addTodo.html',
            RequestContext(request)
        )
def updatetodo(request,id=''):
    if request.method == 'POST':
        atodo = request.POST.get('todo')
        priority = request.POST.get('priority')
        todo = Todo.objects.filter(id=id).update(todo=atodo,priority=priority)
        return HttpResponseRedirect('/todo/todolist')
    else:
        mytodo = Todo.objects.get(id=id)
        return render_to_response("todo/addTodo.html",{'todo':mytodo},RequestContext(request))

