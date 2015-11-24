from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy
from .models import Animal

# Create your views here.

class VerAnimal(ListView):
	model = Animal
	template_name = "index.html"

ver_animal= VerAnimal.as_view()

class AgregarAnimal(CreateView):
   	model = Animal
   	template_name = "crearAnimal.html"
   	fields = "__all__"
   	success_url = reverse_lazy("ver_animal")

crearanimal = AgregarAnimal.as_view()