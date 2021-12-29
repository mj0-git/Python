from typing import List, cast
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from cats.models import Cat, Breed

class MainView(LoginRequiredMixin, ListView):
    model = Cat
    template_name = "cat_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.all().count
        return context


# Create your views here.
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedView(LoginRequiredMixin, ListView):
    model = Breed 
    template_name = 'breed_list.html'

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed 
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed 
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed 
    fields = '__all__'
    success_url = reverse_lazy('cats:all')