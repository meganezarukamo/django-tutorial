# from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from events import models


def create(request):
    title = request.POST.get("title")
    new_event = models.Event()
    new_event.events_title = title
    new_event.save()
    return HttpResponseRedirect(reverse("event:index"))


def index(request):
    all_event = models.Event.objects.all()
    context = {"all_event": all_event}
    return render(request, "events/main.html", context)
