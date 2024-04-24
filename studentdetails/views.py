from django.shortcuts import render
# Create your views here.

from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
def batch_list(request):
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



  
@api_view(['GET'])
def school_list(request):
    if request.method == 'GET':
        school = School.objects.all()
        serializer = SchoolSerializer(school,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def student_add(request):
    if request.method == 'GET':
        student=Student.objects.all()
        serializer =StudentSerializer(student,many = True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)   



@api_view(['GET','POST'])
def batch_add(request):
    if request.method == 'GET':
        batch=Batch.objects.all()
        serializer =BatchSerializer(batch,many = True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','POST'])
def school_add(request):
    if request.method == 'GET':
        school=School.objects.all()
        serializer =SchoolSerializer(school,many = True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)   



@api_view(['GET', 'DELETE'])
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method ==  'GET':
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'DELETE'])
def batch_delete(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    if request.method ==  'GET':
        serializer = BatchSerializer(batch, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def school_delete(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(school, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def student_edit(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH'])
def batch_edit(request, batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchSerializer(batch, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = BatchSerializer(batch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PATCH'])
def school_edit(request, school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = SchoolSerializer(batch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def student_update(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def batch_update(request, batch_id):
    try:
        batch = Batch.objects.get(id=batch_id)
    except Batch.DoesNotExist:
        return Response({'error': 'Batch not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatchSerializer(batch)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer =BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def school_update(request, school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer =SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SchoolWithBatch(APIView):
    def get(self, respect,school_id, format=None):
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response({'error': 'School not found '}, status=status.HTTP_404_NOT_FOUND)
        
        school_serializer = SchoolSerializer(school)
        batch = Batch.objects.filter(school=school)
        final_data = []

        for batch in batch:
           
           batch_serializer = BatchSerializer(batch)
           student_variant = Student.objects.filter(batch=batch)
           variant_serializer = StudentSerializer(student_variant,many=True)

           batch_data = batch_serializer.data
           batch_data['variant']=variant_serializer.data

           final_data.append(batch_data)
       
           

        response_data ={
            'school':school_serializer.data,
           'batch':final_data
        }

        return Response(response_data,status=status.HTTP_200_OK)

# Create your views here.







