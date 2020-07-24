from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# ------------------------------ PointSet Forms ------------------------------

class PointsetCreateForm(forms.Form):
    name = forms.CharField(required=True, label='Point Set Name', min_length=3, max_length=100, help_text='A friendly name to call the point set')
     # Style input
    name.widget.attrs.update({'class':'form-control'})
    # Custom user input validation for attribute: clean_xxx
    def clean_name(self):
        data = self.cleaned_data['name']
        # Make sure that name does not contain a question mark
        if '?' in data:
            raise ValidationError(_('Name must not contain a question mark'))
        return data

class PointsetUpdateForm(forms.Form):
    id = forms.CharField(required=True, label='ID', widget=forms.HiddenInput())
    name = forms.CharField(required=True, label='Point Set Name', min_length=3, max_length=100)
    # Style input
    name.widget.attrs.update({'class':'form-control'})
    # Custom user input validation for attribute: clean_xxx
    def clean_name(self):
        data = self.cleaned_data['name']
        # Make sure that name does not contain a question mark
        if '?' in data:
            raise ValidationError(_('Name must not contain a question mark'))
        return data

class PointsetDeleteForm(forms.Form):
    id = forms.CharField(required=True, label='ID', widget=forms.HiddenInput())


# ------------------------------ Point Forms ------------------------------

class PointCreateForm(forms.Form):
    pointset = forms.CharField(required=True, label='Pointset', widget=forms.HiddenInput())
    name = forms.CharField(required=True, label='Point Name', min_length=1, max_length=100, help_text='A friendly name to call the point')
    latitude = forms.CharField(label='Latitude')
    longitude = forms.CharField(label='Longitude')
    # Style input
    name.widget.attrs.update({'class':'form-control'})
    latitude.widget.attrs.update({'class':'form-control'})
    longitude.widget.attrs.update({'class':'form-control'})
    # Custom user input validation for attribute: clean_xxx
    def clean_name(self):
        data = self.cleaned_data['name']
        # Make sure that name does not contain a question mark
        if '?' in data:
            raise ValidationError(_('Name must not contain a question mark'))
        return data

class PointUpdateForm(forms.Form):
    id = forms.CharField(required=True, label='ID', widget=forms.HiddenInput())
    pointset = forms.CharField(required=True, label='Pointset', widget=forms.HiddenInput())
    name = forms.CharField(required=True, label='Point Name', min_length=1, max_length=100)
    # Style input
    name.widget.attrs.update({'class':'form-control'})
    # Custom user input validation for attribute: clean_xxx
    def clean_name(self):
        data = self.cleaned_data['name']
        # Make sure that name does not contain a question mark
        if '?' in data:
            raise ValidationError(_('Name must not contain a question mark'))
        return data

class PointDeleteForm(forms.Form):
    id = forms.CharField(required=True, label='ID', widget=forms.HiddenInput())
    pointset = forms.CharField(required=True, label='Pointset', widget=forms.HiddenInput())
