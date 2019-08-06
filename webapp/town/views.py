from django.shortcuts import render
from .models import Town
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

class ListTown(ListView):
    model = Town

class CreateTown(CreateView):
    model = Town
    form = Town
    fields = '__all__'

    def get_success_url(self):
        return reverse('list_town')
    
class EditTown(UpdateView):
    model = Town
    form = Town
    fields = '__all__'

    def get_success_url(self):               
        return reverse('list_town')

class DeleteTown(DeleteView):
    model = Town
    form = Town
    fields = '__all__'

    def get_success_url(self):               
        return reverse('list_town')

