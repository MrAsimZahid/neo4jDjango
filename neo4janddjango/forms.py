from django import forms

class PersonForm(forms.Form):
    person_name = forms.CharField(label='name', max_length=100)
    person_age = forms.IntegerField(label='age')
