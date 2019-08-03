
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import (ListTown, EditTown, 
    DeleteTown, CreateTown)

urlpatterns = [
    
    path('list', ListTown.as_view(template_name = "town/index.html"), name = "list"),
    path('create', CreateTown.as_view(template_name = "town/create.html"), name = "create"),
    path('edit/<int:pk>', EditTown.as_view(template_name = "town/edit.html"), name = "edit"),
    path('delete/<int:pk>', DeleteTown.as_view(template_name = "town/delete.html"), name = "delete"),
]