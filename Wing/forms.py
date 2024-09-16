from django import forms
from .models import Wing_One


class Wing_One_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Name of project'}))
    amount_as_per_agreement_currency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'amount as per agreement urrency'}))
    amount_in_equivalent_million_us = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Amount in million'}))
    development_partner = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder':'Development partner'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'type':'text', 'placeholder':'Comments'}))
    
    class Meta:
        model = Wing_One
        fields = '__all__'