from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .models import Item

# Define the home view
class IndexView(ListView):
    model = Item


class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  def form_valid(self, form):
    form.save()  
    return super(ItemCreate, self).form_valid(form) 

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'



