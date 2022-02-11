from django.urls import path
from . import views

urlpatterns = [
	path('', views.TasktodoOverview, name="tasktodo-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
]
