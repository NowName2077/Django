from django.contrib import admin
from .models import Group,Student,Discipline,Mark,StudentDiscipline
# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Discipline)
admin.site.register(Mark)
admin.site.register(StudentDiscipline)
