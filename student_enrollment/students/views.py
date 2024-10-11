from django.shortcuts import render, get_object_or_404, redirect  # Added 'redirect'
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# API Views for CRUD operations
class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Front-end views for rendering templates
def student_list_view(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def student_create_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        course = request.POST['course']
        Student.objects.create(name=name, age=age, course=course)
        return redirect('student-list')  # redirect after successful creation
    return render(request, 'create.html')

def student_update_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.course = request.POST['course']
        student.save()
        return redirect('student-list')  # redirect after successful update
    return render(request, 'update.html', {'student': student})

def student_delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')  # redirect after successful deletion
    return render(request, 'delete.html', {'student': student})