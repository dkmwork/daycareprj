"""sampleprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sampleapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classform',views.classform,name='classform'),
    path('studentform',views.studentform,name='studentform'),
    path('teachersform',views.teachersform,name='teachersform'),
    path('classstudentform',views.classstudentform,name='classstudentform'),
    path('classteachersform',views.classteachersform,name='classteachersform'),
    path('studentlist',views.studentlist,name='studentlist'),
    path('student_edit/<int:studentid>',views.student_edit,name='student_edit'),
    path('class_studentlist',views.class_studentlist,name='class_studentlist'),
    path('classstudent_edit/<int:csid>',views.classstudent_edit,name='classstudent_edit'),
    path('classteachers_bridgelist',views.classteachers_bridgelist,name='classteachers_bridgelist'),
    path('classteachers_edit/<int:ctid>',views.classteachers_edit,name='classteachers_edit'),
    path('check_duplicate',views.check_duplicate,name='check_duplicate'),
    path('check_duplicate1/<str:classname>',views.check_duplicate1,name='check_duplicate1'),
    path('check_class',views.check_class,name='check_class'),
    path('qualificationform',views.qualificationform,name='qualificationform'),
]
