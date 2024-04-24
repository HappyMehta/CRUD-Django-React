from rest_framework import serializers
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    FirstName = serializers.CharField(source='first_name')
    LastName = serializers.CharField(source='last_name')
    Age = serializers.IntegerField(source='age')
    Major = serializers.CharField(source='major')
    class Meta:
        model = Students
        partial=True
        fields =  ('student_id', 'FirstName', 'LastName', 'Age', 'Major')#('student_id',
                #   'first_name',
                #   'last_name',
                #   'age',
                #   'major')