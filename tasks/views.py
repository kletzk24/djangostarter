from django.shortcuts import render

from .models import Task
from .models import Member
from .models import Notification

# Create your views here.
def listtasks(request, project):
    tasks = Task.objects.filter(project__name=project)

    return render (request, "tasks/listtasks.html", {
        'project': project,
        'tasks': tasks
    })

def listnotifications(request, member):
    try:
        notifications = Member.objects.filter(username=member)[0].notification_set.all()

        if notifications.length > 0:
            return render(request, "tasks/listnotifications.html", {
                'member': member,
                'output': 1,
                'notifications': notifications
            })
        else:
            return render(request, "tasks/listnotifications.html", {
            'member': member,
            'output': 2,
        })
    except:
        return render(request, "tasks/listnotifications.html", {
            'member': member,
            'output': 3
        })
    