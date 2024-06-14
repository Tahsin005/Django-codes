from rest_framework import serializers
from . models import Student

# Validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with r')

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = '__all__'    
    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seats are full')
        return value
    
    # Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('Rohit can only live in Ranchi')
        return data