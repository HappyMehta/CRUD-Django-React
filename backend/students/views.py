from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Students
from .serializers import StudentSerializer


class StudentView(APIView):

    def get_student(self, pk):
        try:
            student = Students.objects.get(student_id=pk)
            return student
        except Students.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else:
            data = Students.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Added Successfully", safe=False)
        return JsonResponse("Failed to Add Student", safe=False)

    def put(self, request, pk=None):
        student_to_update = Students.objects.get(student_id=pk)
        serializer = StudentSerializer(instance=student_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student updated Successfully", safe=False)
        return JsonResponse("Failed To Update Student")
    def delete(self, request, pk):
        student_to_delete = Students.objects.get(student_id=pk)
        student_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)

