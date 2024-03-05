from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField(label='Age') 
    weight = forms.FloatField(label='Weight')
    balance = forms.DecimalField(label='Balance')