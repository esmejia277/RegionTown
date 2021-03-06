from django.shortcuts import render
from .models import Region
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django import forms


class ListRegion(ListView):
    model = Region

class DeleteRegion(DeleteView):
    model = Region
    form = Region
    fields = '__all__'

    def get_success_url(self):               
        return reverse('list_region')

class EditRegion(UpdateView):
    model = Region
    form = Region
    fields = '__all__'

    def get_success_url(self):               
        return reverse('list_region')