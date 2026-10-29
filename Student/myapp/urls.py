from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name ='about'),
    path('students/', views.students, name ='students'),
    path('students/get/', views.get_students, name='GetStudents'),
    path('students/filter/', views.filter_students, name='FilterStudents'),
    path('students/sort/', views.sort_students, name='SortStudents'),
    path('students/query/', views.query_students, name='QueryStudents'),
]