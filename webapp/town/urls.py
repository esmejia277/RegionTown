
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import (ListTown, EditTown, 
    DeleteTown, CreateTown)

urlpatterns = [
    
    path('list_town', ListTown.as_view(template_name = "town/list.html"), name = "list_town"),
    path('create_town', CreateTown.as_view(template_name = "town/create.html"), name = "create_town"),
    path('edit_town/<int:pk>', EditTown.as_view(template_name = "town/edit.html"), name = "edit_town"),
    path('delete_town/<int:pk>', DeleteTown.as_view(template_name = "town/delete.html"), name = "delete_town"),
]