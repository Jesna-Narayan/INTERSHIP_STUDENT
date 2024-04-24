from rest_framework import serializers
from .models import School
from .models import Batch
from .models import Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Student
       fields = '__all__'


