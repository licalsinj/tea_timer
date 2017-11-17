# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Tea, WesternBrew, GongFuBrew
from .forms import GongFuBrewForm, TeaForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import re
import numpy as np
from django.http import JsonResponse

# Create your views here.


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'tea/index.html')
    else:
        teas = Tea.objects.filter(user=request.user)
        brew_results = GongFuBrew.objects.all()
        query = request.GET.get("q")
        if query:
            tea = tea.filter(
                Q(tea__name__icontains =query) |
                Q(tea__type__icontains=query)
            ).distinct()
            brew_results = brew_results.filter(
                Q(tea__gongfubrew__brew_name__icontains=query)
            ).distinct()
            return render(request, 'tea/index.html', {
                'tea': tea,
                'brew': brew_results,
            })
        else:
            return render(request, 'tea/index.html', {'all_teas': teas})


class DetailView(generic.DetailView):
    model = Tea
    template_name = 'tea/details.html'


def create_tea(request):
    if not request.user.is_authenticated():
        return redirect('login')
    else:
        form = TeaForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            tea = form.save(commit=False)
            tea.user = request.user
            tea.save()
            return render(request, 'tea/details.html', {'tea': tea})
        context = {
            "form": form,
        }
    return render(request, 'tea/tea_form.html', context)


'''
class TeaCreate(CreateView):
    model = Tea
    model.objects.all()
    fields = ['name', 'type', 'price', 'rating', 'picture', 'origin', 'tasting_notes']
    template_name_suffix = '_form'

    def as_view(request):
        if not request.user.is_authenticated():
            return render(request, 'tea/registration/login.html')
        else:
            CreateView.as_view(request)
'''


class TeaUpdate(UpdateView):
    model = Tea
    fields = ['name', 'type', 'price', 'rating', 'picture', 'origin', 'tasting_notes']
    template_name_suffix = '_form'

    
class TeaDelete(DeleteView):
    model = Tea
    success_url = reverse_lazy('tea:index')


'''def update_gfbrew(request, pk):
    form = GongFuBrewForm(request.POST or None)
    brew = get_object_or_404(GongFuBrew, pk=pk)
    if form.is_valid():
        brew_form = form.save(commit=False)
        steep_times_string = form.clean_steep_times_string()
        str_steep_times = re.split(',+', steep_times_string)
        lst_steep_times = [int(x) for x in str_steep_times]
        brew.steep_times = np.asarray(lst_steep_times)
        brew.steep_num = len(brew.steep_times)
        brew.save()
        return HttpResponseRedirect(reverse('tea:detail', args=[brew.tea.id]))
    context = {
        'tea': brew.tea,
        'brew': brew,
        'form': form,
        'title': "Update " + brew.brew_name
    }
    return render(request, 'tea/gongfubrew_form.html', context)'''


'''def update_gfbrew(request, pk):
    form = GongFuBrewForm(request.POST or None)
    brew = get_object_or_404(GongFuBrew, pk=pk)
    form.tea = brew.tea
    form.brew_name = brew.brew_name
    form.gaiwan_size = brew.gaiwan_size
    form.temp_C = brew.temp_C
    form.tea_qty = brew.tea_qty
    form.steep_times_string = brew.steep_times_string
    form.fields.brew_name = brew.brew_name
    if form.is_valid():
        brew = form.save(commit=False)
        brew.save()
        return HttpResponseRedirect(reverse('tea:detail', args=str(brew.tea.id)))
    context = {
        'brew': brew,
        'tea': brew.tea,
        'form': form,
        'title': "Update " + brew.brew_name,
    }
    return render(request, 'tea/gongfubrew_form.html', context)'''


class GongFuBrewUpdate(UpdateView):
    model = GongFuBrew
    fields = ['brew_name', 'gaiwan_size', 'temp_C', 'tea_qty', 'steep_times_string']
    template_name = 'tea/gongfubrew_form.html'

    def get_success_url(self):
        brew = GongFuBrew.objects.get(id=self.kwargs["pk"])
        return reverse_lazy('tea:detail', args=[brew.tea_id])

    def form_valid(self, form):
        steep_times_string = form.clean_steep_times_string()
        return super(GongFuBrewUpdate, self).form_valid(form)


def delete_gfbrew(request, brew_id):
    brew = get_object_or_404(GongFuBrew, pk=brew_id)
    tea_id = brew.tea.id
    brew.delete()
    return HttpResponseRedirect(reverse('tea:detail', args=[tea_id]))


def create_gfbrew(request, tea_id):
    form = GongFuBrewForm(request.POST or None, request.FILES or None)
    tea = get_object_or_404(Tea, pk=tea_id)
    if form.is_valid():
        brew = form.save(commit=False)
        brew.tea = tea
        steep_times_string = form.clean_steep_times_string()
        str_steep_times = re.split(',+', steep_times_string)
        lst_steep_times = [int(x) for x in str_steep_times]
        brew.steep_times = np.asarray(lst_steep_times)
        brew.steep_num = len(brew.steep_times)
        brew.save()
        return HttpResponseRedirect(reverse('tea:detail', args=[brew.tea.id]))
    context = {
        'tea': tea,
        'form': form,
    }
    return render(request, 'tea/gongfubrew_form.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('tea:index')
    else:
        form = RegisterForm()
    return render(request, 'tea/registration/register.html', {'form': form})
