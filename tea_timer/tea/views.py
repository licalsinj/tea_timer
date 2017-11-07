# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Tea, WesternBrew, GongFuBrew
from .forms import GongFuBrewForm, TeaForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'tea/index.html'
    context_object_name = 'all_teas'

    def get_queryset(self):
        return Tea.objects.all()


class DetailView(generic.DetailView):
    model = Tea
    template_name = 'tea/details.html'
    
    
class TeaCreate(CreateView):
    model = Tea
    model.objects.all()
    fields = ['name', 'type', 'price', 'rating', 'picture', 'origin', 'tasting_notes']
    template_name_suffix = '_form'


class TeaUpdate(UpdateView):
    model = Tea
    fields = ['name', 'type', 'price', 'rating', 'picture', 'origin', 'tasting_notes']
    template_name_suffix = '_form'

    
class TeaDelete(DeleteView):
    model = Tea
    success_url = reverse_lazy('tea:index')


class GongFuBrewCreate(CreateView):
    model = GongFuBrew
    fields = ['brew_name', 'gaiwan_size', 'temp_C', 'tea_qty', 'steep_num', 'steep_times']

'''
class GongFuBrewUpdate(UpdateView):
    model = GongFuBrew
    form_class = GongFuBrewForm
    fields = ['brew_name', 'gaiwan_size', 'temp_C', 'tea_qty', 'steep_num', 'steep_times']
    form_class = GongFuBrewForm
    template_name = 'tea/gongfubrew_form.html'
'''


class GongFuBrewDelete(DeleteView):
    model = GongFuBrew
    success_url = reverse_lazy('tea:detail')


def create_gfbrew(request, tea_id):
    form = GongFuBrewForm(request.POST or None, request.FILES or None)
    tea = get_object_or_404(Tea, pk=tea_id)
    if form.is_valid():
        brew = form.save(commit=False)
        brew.tea = tea
        brew.save()
        return HttpResponseRedirect(reverse('tea:detail', args=str(tea.id)))
    context = {
        'tea': tea,
        'form': form,
    }
    return render(request, 'tea/gongfubrew_form.html', context)


def update_gfbrew(request, brew_id):
    form = GongFuBrewForm(request.POST or None, request.FILES or None)
    brew = get_object_or_404(GongFuBrew, pk=brew_id)
    form.brew_name = brew.brew_name
    if form.is_valid():
        brew = form.save(commit=False)
        brew.save()
        return HttpResponseRedirect(reverse('tea:detail', args=str(brew.tea.id)))
    context = {
        'brew': brew,
        'tea': brew.tea,
        'form': form,
    }
    return render(request, 'tea/gongfubrew_form.html', context)




