from django.shortcuts import render

from .models import Task

# Create your views here.
def listtasks(request, project):
    tasks = Task.objects.filter(project__name=project)

    return render (request, "tasks.listtasks.html", {
        'project': project,
        'tasks': tasks
    })