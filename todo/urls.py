from django.urls import path

from . import views

app_name = "todo"
urlpatterns = [
    path("list/", views.list, name="list"),
    path("edit/", views.edit, name="edit"),
    # path("edit/<int:todo_id>/update", views.update, name="update"),
    # path("create/", views.create, name="create"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("list2/", views.list2, name="list2"),
    path("edit2/", views.edit2, name="edit2"),
]
