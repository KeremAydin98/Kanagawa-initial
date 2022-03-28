from django.views.generic import TemplateView, ListView, DetailView
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    current_object_name = 'product_list'


class AboutPageView(TemplateView):
    model = Product
    template_name = 'about.html'


class DetailPageView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class CreatePageView(CreateView,LoginRequiredMixin):
    model = Product
    template_name = 'product_new.html'
    fields = ['product_name', 'product_price', 'currency', 'product_description','user']


class UpdatePageView(UpdateView,LoginRequiredMixin):
    model = Product
    template_name = 'product_edit.html'
    fields = ['product_name', 'product_price', 'currency', 'product_description']


class DeletePageView(DeleteView,LoginRequiredMixin):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')
