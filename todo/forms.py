from django import forms
from django.utils import timezone


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
        widget = forms.TextInput(
            attrs = {'class':'form-control','placeholder':'What needs to be done?', 'aria-label':'Todo','arial-describedby':'add-btn'}))
    due_date = forms.CharField(max_length=40,
        widget = forms.TextInput(
            attrs = {'class':'form-control','placeholder':'By when it needs to be completed?', 'aria-label':'Todo','arial-describedby':'add-btn'}))
