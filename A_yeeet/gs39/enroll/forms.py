from django import forms 

class StudentRegistration(forms.Form):
    # name = forms.CharField(min_length=5, max_length=50,strip=False)
    # name = forms.CharField(empty_value='Tahsin')
    name = forms.CharField(error_messages={
        'required': 'Enter your name'
    })
    agree = forms.BooleanField(label='I Agree', label_suffix=' ')
    roll = forms.IntegerField(min_value=5, max_value=40)
    price = forms.DecimalField(min_value=5, max_value=40, max_digits=4, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=40)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=50)
    website = forms.URLField(min_length=5, max_length=50)
    password = forms.CharField(min_length=5, max_length=50, widget=forms.PasswordInput)
    description = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={
        'class' : 'somecss1 somecss2',
        'id' : 'uniqueid',
    }))
    notes = forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 3,
        'cols' : 50,
    }))