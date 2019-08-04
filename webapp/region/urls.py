
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import (ListRegion, DeleteRegion, EditRegion)

urlpatterns = [
    path('list_region', ListRegion.as_view(template_name = "region/list.html"), name = "list_region"),
    # path('create', CreateTown.as_view(template_name = "town/create.html"), name = "create_region"),
    path('edit_region/<int:pk>', EditRegion.as_view(template_name = "region/edit.html"), name = "edit_region"),
    path('delete_region/<int:pk>', DeleteRegion.as_view(), name = "delete_region"),
]