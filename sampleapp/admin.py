from django.contrib import admin
from sampleapp.models import Classes,Student,Teachers,Class_Student_Bridge,Class_Teachers_Bridge,Qualification,Teacher_Qualification_Bridge

admin.site.register(Classes)
admin.site.register(Student)
admin.site.register(Teachers)
admin.site.register(Class_Teachers_Bridge)
admin.site.register(Class_Student_Bridge)
admin.site.register(Qualification)
admin.site.register(Teacher_Qualification_Bridge)

# Register your models here.
