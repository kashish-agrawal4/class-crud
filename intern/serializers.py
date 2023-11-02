from rest_framework import serializers
from .models import Intern

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['emp_id','name', 'clg_name', 'age', 'passing_year', 'address', 'phone_number', 'finishing_date']
