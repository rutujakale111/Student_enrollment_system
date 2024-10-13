from django.urls import path
from .views import StudentViewSet, student_list_view, student_create_view, student_update_view, student_delete_view

student_list = StudentViewSet.as_view({'get': 'list'})
student_create = StudentViewSet.as_view({'post': 'create'})
student_detail = StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    
    path('students/', student_list, name='student-list-api'),
    path('students/create/', student_create, name='student-create-api'),
    path('students/<int:pk>/', student_detail, name='student-detail-api'),

    
    path('', student_list_view, name='student-list'),
    path('create/', student_create_view, name='student-create'),
    path('update/<int:pk>/', student_update_view, name='student-update'),
    path('delete/<int:pk>/', student_delete_view, name='student-delete'),
]