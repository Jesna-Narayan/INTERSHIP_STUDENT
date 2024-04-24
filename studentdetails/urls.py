from django.urls import path
from studentdetails.views import *

urlpatterns =[
  path('student/list',student_list,name='student_list'),
  path('batch/list',batch_list,name='batch_list'),
  path('school/list',school_list,name='school_list'),
  path('student/add',student_add,name = 'student_add'),
  path('batch/add',batch_add,name = 'batch_add'),
  path('school/add',school_add,name = 'school_add'),
  path('student/<int:student_id>/delete/', student_delete, name='student-delete'),
  path('batch/<int:batch_id>/delete/', batch_delete, name='batch-delete'),
  path('school/<int:school_id>/delete/', school_delete, name='school-delete'),
  path('student/<int:student_id>/edit/', student_edit, name='student-edit'),
  path('batch/<int:batch_id>/edit/', batch_edit, name='batch-edit'),
  path('school/<int:school_id>/edit/', school_edit, name='school-edit'),
  path('student/<int:student_id>/update/', student_update, name='student-update'),
  path('batch/<int:batch_id>/update/', batch_update, name='batch-update'),
  path('school/<int:school_id>/update/', school_update, name='school-update'),
]

