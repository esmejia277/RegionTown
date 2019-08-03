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

class CreateTown(CreateView, SuccessMessageMixin):
    model = Town
    form = Town
    fields = '__all__'
    success_message = 'Town created successfully'

    def get_success_url(self):
        return reverse('list')
    
class EditTown(UpdateView, SuccessMessageMixin):
    model = Town
    form = Town
    fields = '__all__'
    success_message = 'Town updated successfully'

    def get_success_url(self):               
        return reverse('list')

class DeleteTown(DeleteView, SuccessMessageMixin):
    model = Town
    form = Town
    fields = '__all__'

    def get_success_url(self):               
        return reverse('list')


# Create your views here.
