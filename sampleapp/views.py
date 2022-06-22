from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Q, Count
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from sampleapp.models import Classes,Student,Teachers,Class_Student_Bridge,Class_Teachers_Bridge,Qualification,Teacher_Qualification_Bridge
from sampleapp.forms import ClassModelForm,StudentModelForm,TeachersModelForm,ClassStudent_ModelForm,ClassTeachers_ModelForm,QualificationModelForm

def classform(request):
    template_name="sampleapp/classform.html"
    classmodelform=ClassModelForm()
    context={"MyClass":classmodelform}
    if request.method=="GET":
        return render(request,template_name,context)
    elif request.method=="POST":
        classmodelform=ClassModelForm(request.POST)
        if classmodelform.is_valid():
            classmodelform.save()
            classmodelform=ClassModelForm()
            context={"MyClass":classmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def check_duplicate(request):
    if request.method =="GET":
        print('hi')
        classname=request.GET.get('classname')
        print(classname)
        class_obj= Classes.objects.filter(class_name__exact=classname)
        if len(class_obj)==0:
            x=0
        else:
            x=1
        return JsonResponse(x,safe=False)

def check_duplicate1(request,classname):
    if request.method =="GET":
        print('hi')
        
        print(classname)
        class_obj= Classes.objects.filter(class_name__exact=classname)
        if len(class_obj)==0:
            x=0
        else:
            x=1
        return JsonResponse(x,safe=False)

def check_class(request):
    new_dict={}
    ref_year = 2022
    if request.method =="GET":
        dob=request.GET.get('student_dob')
        dob=int(dob.split('/')[2])
        x = ref_year-dob
        class_obj=Classes.objects.get(min_age=x)
        new_dict['class_name']=class_obj.class_name
        print(class_obj.max_student)
        student_class=Class_Student_Bridge.objects.filter(classname=class_obj.class_id)
        print(student_class)

        return JsonResponse(new_dict,safe=False)
    
'''def select_student(request):
    if request.method == "GET":
        classname=request.GET.get('classname')
        classobj= Classes.objects.get(class_name=classname)
        studentobj=Student.objects.all().values('student_dob')
        student_year=student_obj('student_dob').year()'''

def studentform(request):
    template_name="sampleapp/studentform.html"
    studentmodelform=StudentModelForm()
    context={"MyStudent":studentmodelform}
    if request.method=="GET":
        return render(request,template_name,context)
    elif request.method=="POST":
        studentmodelform=StudentModelForm(request.POST)
        if studentmodelform.is_valid():
            studentmodelform.save()
            student_obj = Student.objects.latest('student_id')
            #student=Student.objects.get(student_id=student_obj)
            class_student_model=Class_Student_Bridge()
            class_student_model.student=student_obj
            class_student_model.classname=studentmodelform.cleaned_data['student_class']
            class_student_model.save()
            studentmodelform=StudentModelForm()
            context={"MyStudent":studentmodelform}
            return render(request,template_name,context)
        else:
            context={"MyStudent":studentmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)
def qualificationform(request):
    template_name="sampleapp/qualificationform.html"
    qualificationmodelform=QualificationModelForm()
    context={"MyQualification":qualificationmodelform}
    if request.method=="GET":
        return render(request,template_name,context)
    elif request.method=="POST":
        qualificationmodelform=QualificationModelForm(request.POST)
        if qualificationmodelform.is_valid():
            qualificationmodelform.save()
            qualificationmodelform=QualificationModelForm()
            context={"MyQualification":qualificationmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def teachersform(request):
    template_name="sampleapp/teachersform.html"
    teachersmodelform=TeachersModelForm()
    context={"MyTeacher":teachersmodelform}
    if request.method=="GET":
        return render(request,template_name,context)
    elif request.method=="POST":
        teachersmodelform=TeachersModelForm(request.POST)
        qualifications=request.POST.getlist('quali_id')
        '''techername=request.POST('teacher_name')
        contact=request.POST.get('contact_no')
        emil=request.POST.get('teachers_email')
        yearexpe=request.POST.get('years_experience')
        for item in qualifications:
            teachersobj=Teachers()
            teachersobj.teacher_name=techername
            teachersobj.contact_no=request.POST.get('contact_no')
            teachersobj.teachers_email=request.POST.get('teachers_email')
            teachersobj.years_experience=request.POST.get('years_experience')
            teachersobj.qualifications=Qualification.objects.get(quali_id=item)
            teachersobj.save()'''
        if teachersmodelform.is_valid():
            teachersmodelform.save()
            latest_teacherid=Teachers.objects.last()
            latest_teacherobj=Teachers.objects.get(teacher_id=latest_teacherid.teacher_id)
            for item in qualifications:
                teachersobj=Teacher_Qualification_Bridge()
                teachersobj.teacher=latest_teacherobj
                teachersobj.qualification=Qualification.objects.get(quali_id=item)
                teachersobj.save()
            teachersmodelform=TeachersModelForm()
            context={"MyTeacher":teachersmodelform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def classstudentform(request):
    template_name="sampleapp/classstudentform.html"
    classstudentform=ClassStudent_ModelForm()
    context={"MyClassStudent":classstudentform}
    if request.method=="GET":
        return render(request,template_name,context)
    elif request.method=="POST":
        classstudentform=ClassStudent_ModelForm(request.POST)

        if classstudentform.is_valid():
            
            classstudentform.save()
            classstudentform=ClassStudent_ModelForm()
            context={"MyClassStudent":classstudentform}
            return render(request,template_name,context)
        else:
            print(classstudentform.errors)
            context={"MyClassStudent":classstudentform}
            return render(request,template_name,context)
        
    return render(request,template_name,context)

def classteachersform(request):
    template_name="sampleapp/classteachersform.html"
    classteachersform=ClassTeachers_ModelForm()
    context={"MyClassTeacher":classteachersform}
    if request.method=="GET":
        return render(request,template_name,context)
    elif request.method=="POST":
        classteachersform=ClassTeachers_ModelForm(request.POST)
        if classteachersform.is_valid():
            classteachersform.save()
            classteachersform=ClassTeachers_ModelForm()
            context={"MyClassTeacher":classteachersform}
            return render(request,template_name,context)
    return render(request,template_name,context)

def studentlist(request):
    template_name="sampleapp/studentlist.html"
    if request.method=="GET":
        print(request.GET)
        query=Q()
        page_num=request.GET.get('page',1)
        student_name=request.GET.get('student_name','')
        print(student_name)
        if student_name !='':
            query &=Q(student_name__contains=student_name)
        #print(query)
        if query != '(AND: )':
            studentlist= Student.objects.filter(query).order_by('student_name')
        else: 
            studentlist=Student.objects.all().order_by('student_name')
        paginator=Paginator(studentlist,2)
        page_number=request.GET.get('page',1)
        page_obj=paginator.get_page(page_number)
        context={"page_obj":page_obj,"Student":student_name}
    return render(request,template_name,context)

def student_edit(request,studentid=None):
    template_name="sampleapp/studentinfo.html"
    if request.method=="GET" and studentid != None:
        studentobjectmodel=Student.objects.get(student_id=studentid)
        studentobjectmodelform=StudentModelForm(instance=studentobjectmodel)
        context={"studentobjectinstance":studentobjectmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and studentid != None:
        studentobjectmodel=Student.objects.get(student_id=studentid)
        studentobjectmodelform=StudentModelForm(request.POST,instance=studentobjectmodel)
        if studentobjectmodelform.is_valid():
            studentobjectmodelform.save()
            studentobjectmodelform=StudentModelForm()
            context={"studentobjectinstance":studentobjectmodelform}
            return render(request,template_name,context)
    studentobjectmodelform=StudentModelForm()
    context={"studentobjectinstance":studentobjectmodelform}
    return render(request,template_name,context)

def class_studentlist(request):
    template_name="sampleapp/class_studentlist.html"
    if request.method=="GET":
        query= Q()
        page_num=request.GET.get('page',1)
        class_name=request.GET.get('class_name','')
        student_name=request.GET.get('student_name','')
        if class_name != '':
            query &=Q(classname__class_name__contains=class_name)
        if student_name != '':
            query &=Q(student__student_name__contains=student_name)
        if query != '(AND: )':
            classstudentlist=Class_Student_Bridge.objects.filter(query).order_by('classname')
        else:
            classstudentlist=Class_Student_Bridge.objects.all().order_by('classname')
        paginator=Paginator(classstudentlist,2)
        page_number=request.GET.get('page',1)
        page_obj=paginator.get_page(page_number)
        context={"page_obj":page_obj,"Classname":class_name,"Student":student_name}
    return render(request,template_name,context)
def classstudent_edit(request,csid=None):
    template_name="sampleapp/classstudentinfo.html"
    if request.method=="GET" and csid !=None:
        classstudentsubjectmodel=Class_Student_Bridge.objects.get(cs_bridgeid=csid)
        classstudentsubjectmodelform=ClassStudent_ModelForm(instance=classstudentsubjectmodel)
        context={"classstudentinstance":classstudentsubjectmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and csid != None:
        classstudentsubjectmodel=Class_Student_Bridge.objects.get(cs_bridgeid=csid)
        classstudentsubjectmodelform=ClassStudent_ModelForm(request.POST,instance=classstudentsubjectmodel)
        if classstudentsubjectmodelform.is_valid():
            classstudentsubjectmodelform.save()
            classstudentsubjectmodelform=ClassStudent_ModelForm()
            context={"classstudentinstance":classstudentsubjectmodelform}
            return render(request,template_name,context)
    classstudentsubjectmodelform=ClassStudent_ModelForm()
    context={"classstudentinstance":classstudentsubjectmodelform}
    return render(request,template_name,context)

def classteachers_edit(request,ctid=None):
    template_name="sampleapp/classteachersinfo.html"
    if request.method =="GET" and ctid != None:
        classteacherssubjectmodel=Class_Teachers_Bridge.objects.get(ct_bridgeid=ctid)
        classteacherssubjectmodelform=ClassTeachers_ModelForm(instance=classteacherssubjectmodel)
        context={"classteachersinstance":classteacherssubjectmodelform}
        return render(request,template_name,context)
    elif request.method=="POST" and ctid != None:
        classteacherssubjectmodel=Class_Teachers_Bridge.objects.get(ct_bridgeid=ctid)
        classteacherssubjectmodelform=ClassTeachers_ModelForm(request.POST,instance=classteacherssubjectmodel)
        if classteacherssubjectmodelform.is_valid():
            classteacherssubjectmodelform.save()
            classteacherssubjectmodelform =ClassTeachers_ModelForm()
            context={"classteachersinstance":classteacherssubjectmodelform}
            return render(request,template_name,context)
    classteacherssubjectmodelform =ClassTeachers_ModelForm()
    context={"classteachersinstance":classteacherssubjectmodelform}
    return render(request,template_name,context)

def classteachers_bridgelist(request):
    template_name="sampleapp/classteacherslist.html"
    if request.method=="GET":
        query= Q()
        page_num=request.GET.get('page',1)
        classname=request.GET.get('classname','')
        teachers=request.GET.get('teachersname','')
        if classname != '':
            query &=Q(classname__class_name__contains=classname)
        if teachers != '':
            query &=Q(teacher__teacher_name__contains=teachers)
        if query != '(AND : )':
            classteachersobjectlist=Class_Teachers_Bridge.objects.filter(query).order_by('classname')
        else:
            classteachersobjectlist=Class_Teachers_Bridge.objects.all().order_by('classname')
        paginator=Paginator(classteachersobjectlist,2)
        page_number=request.GET.get('page',1)
        page_obj=paginator.get_page(page_number)
        context={"page_obj":page_obj,"Classname":classname,"Teachers":teachers}
    return render(request,template_name,context)









    








# Create your views here.
