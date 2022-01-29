from django import forms
from .models import *


class Brandform(forms.ModelForm):
    class Meta:
        model = menu
        fields = "__all__"
