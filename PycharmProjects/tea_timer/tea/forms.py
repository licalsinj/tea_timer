from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField
import re
from django.utils.translation import gettext as _
from .models import Tea, GongFuBrew, WesternBrew


class TeaForm(forms.ModelForm):

    class Meta:
        model = Tea
        fields = ['name', 'type', 'price', 'rating', 'picture', 'origin', 'tasting_notes']


class GongFuBrewForm(forms.ModelForm):
    tea = Tea()
    brew_name = forms.CharField(max_length=100)
    gaiwan_size = forms.FloatField()
    temp_C = forms.IntegerField()
    tea_qty = forms.FloatField()
    steep_num = forms.HiddenInput()
    steep_times_string = forms.CharField()
    steep_times = forms.HiddenInput()

    class Meta:
        model = GongFuBrew
        fields = ('brew_name', 'gaiwan_size', 'temp_C', 'tea_qty', 'steep_times_string')

    def clean_steep_times_string(self):
        steep_times_string = self.cleaned_data['steep_times_string']
        pattern = re.compile(r'^[0-9]+(,[0-9]+)*$')
        if not pattern.match(steep_times_string):
            raise ValidationError(_("Please enter numbers separated by commas. Ex: 15,30,45,60"),
                                  code='csv_steep_times_string')
        return steep_times_string


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

