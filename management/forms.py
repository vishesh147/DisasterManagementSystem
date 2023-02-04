from django.forms import ModelForm
from .models import Organization, Volunteer, Resource
from django.forms import CheckboxSelectMultiple, TextInput, NumberInput, Select, SelectMultiple


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        exclude = ['user']
        widgets = {
            'locations': SelectMultiple(attrs={"class":"form-select my-2 mb-3"}),
            'domain': TextInput(attrs={"class":"form-control my-2 mb-3"}),
            'level': Select(attrs={"class":"form-select my-2 mb-3"}),
        }


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        exclude = ['user', 'availability']
        widgets = {
            'organization': Select(attrs={"class":"form-select my-2 mb-3"}),
            'age': NumberInput(attrs={"class":"form-control my-2 mb-3"}),
            'sex': Select(attrs={"class":"form-select my-2 mb-3"}),
            'skills': CheckboxSelectMultiple(attrs={"class":"my-1"}),
            'city': Select(attrs={"class":"form-select my-2 mb-3"}),
        }


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        exclude = ['resourceID', 'organization']
        widgets = {
            'name': TextInput(attrs={"class":"form-control my-2 mb-3"}),
            'quantity':TextInput(attrs={"class":"form-control my-2 mb-3"}),
            'city':Select(attrs={"class":"form-control my-2 mb-3"}),
            'ward':NumberInput(attrs={"class":"form-control my-2 mb-3"})
        }