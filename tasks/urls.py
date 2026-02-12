from django.urls import path
from . import views

app_name="tasks"

urlpatterns = [
    # path("compute/<int:value>", views.compute, name="compute"),
    path("listtasks/<str:project>/", views.listtasks, name="listtasks"),
    path("listnotifications/<str:member>/", views.listnotifications, name="listnotifications"),
]