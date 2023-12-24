from django import forms
from . import models

class WriteForm(forms.ModelForm):

    class Meta:
        model = models.WriteModel
        fields = ['title','description']
        