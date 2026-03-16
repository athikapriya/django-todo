# third party imports
from django.urls import path

# local imports
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("toggle/<int:pk>/", views.toggle_complete, name="toggle_complete"),
    path("create_task/", views.create_task, name="create_task"),
    path("update_task/<int:pk>/", views.update_task, name="update_task"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
]
