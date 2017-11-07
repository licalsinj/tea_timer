from django import forms
from django.contrib.auth.models import User

from .models import Tea, GongFuBrew, WesternBrew


class TeaForm(forms.ModelForm):

    class Meta:
        model = Tea
        fields = ['name', 'type', 'price', 'rating', 'picture', 'origin', 'tasting_notes']


class GongFuBrewForm(forms.ModelForm):

    class Meta:
        model = GongFuBrew
        fields = ['brew_name', 'gaiwan_size', 'temp_C', 'tea_qty', 'steep_num', 'steep_times']