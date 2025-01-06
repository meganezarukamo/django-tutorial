from django.shortcuts import render
from django.http import HttpResponse

from todo import models


def list(request):
    # データの登録
    new_todo = models.Todo()
    new_todo.todo_title = title
    new_todo.save()
    # return HttpResponseRedirect(reverse("todo.list"))

    # 　データの取得
    all_todo = models.Todo.objects.all()
    context = {"todos": all_todo}
    return render(request, "index.html", context)


def edit(request,todo_id):
    return HttpResponse("edit")


def delete(request,todo_id):
    target_todo = models.Todo.objects.get(id=todo_id)


def list2(request):
    return HttpResponse("list2")


def edit2(request):
    return HttpResponse("edit2")
