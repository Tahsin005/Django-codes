from django import forms
from first_app.models import StudentModel
# Create your forms here.
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exclude = ['roll']
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : 'Enter Student Name',
            'roll' : 'Enter Student Roll'
        }
        error_messages = {
            'name' : {'required': 'Your name is required'}
        }