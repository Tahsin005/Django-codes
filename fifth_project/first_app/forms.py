from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name', help_text='Total length must be within 50 Characters', required=False, widget = forms.Textarea(attrs={'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'}))
    # files = forms.FileField()
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField(label='Age') 
    # weight = forms.FloatField(label='Weight')
    # balance = forms.DecimalField(label='Balance')
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField(label='Check')
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    # appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    

class studentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.EmailInput)
    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 10:
            raise forms.ValidationError('Name must be greater than 10')
        return valname