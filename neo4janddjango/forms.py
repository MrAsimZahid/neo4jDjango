from django import forms
from django.forms import TextInput, NumberInput

# class PersonForm(forms.Form):
#     person_name = forms.CharField(label='name', max_length=100)
#     person_age = forms.IntegerField(label='age')


class PersonForm(forms.Form):
    person_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    person_age = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' :'Age', 'style': 'width: 300px;', 'class': 'form-control'}))


class CityForm(forms.Form):
    city_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    city_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Code: PKR', 'style': 'width: 300px;', 'class': 'form-control'}))


class FriendForm(forms.Form):
    f1_uid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter UID', 'style': 'width: 300px;', 'class': 'form-control'}))
    f2_uid = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter UID', 'style': 'width: 300px;', 'class': 'form-control'}))