from django import forms
from django.forms import ModelForm
from django_select2 import forms as select2forms
from django.db.models import  Count
from sampleapp.models import Classes,Student,Teachers,Class_Student_Bridge,Class_Teachers_Bridge,Qualification

def checking_age(age_till_year,year_obj,min_age,max_age):
    student_age = age_till_year - year_obj
    if min_age > student_age or student_age > max_age:
        return True

class ClassModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['class_name'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Classes
        exclude=('class_id',)

class StudentModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['student_name'].widget.attrs.update({'autofocus':'autofocus'})
        self.fields["student_dob"]=forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker','autocomplete':'off'}))
    class Meta:
        model=Student
        exclude=('student_id',)
    
class QualificationModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['qualification'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Qualification
        exclude=('quali_id',)

class TeachersModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['teacher_name'].widget.attrs.update({'autofocus':'autofocus'})
        self.fields['qualifications']=forms.ModelMultipleChoiceField(queryset=Qualification.objects.all())
        self.fields['qualifications'].widget.attrs.update({'class':'select2','multiple':'multiple'})
        #self.fields['qualifications']=forms.ModelMultipleChoiceField(widget=select2forms.Select2MultipleWidget(attrs={'class':'select2','multiple':'multiple'}),queryset=Qualification.objects.all())
    class Meta:
        model=Teachers
        exclude=('teacher_id',)


class ClassStudent_ModelForm(ModelForm):
    # function for checking the class strength and student in the class (from class_student_bridge).
    def check_initialvalues():
        class_strength=Classes.objects.annotate(class_count=Count('class_student_bridge__classname'))
        # class_list=list()
        # class_list.append(('0','-----------'))
        # for instance in class_strength:
        #     if instance.max_student > instance.class_count:
        #         class_list.append((instance.class_id,instance.class_name))
        return class_strength
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['classname'].widget.attrs.update({'autofocus':'autofocus'})
        # using static method
        new_list=ClassStudent_ModelForm.check_initialvalues()
        print(new_list)
        self.fields['classname']=forms.ModelChoiceField(queryset=new_list.filter(class_count__lte=0))
        

    def clean(self):
        cleaned_data=super().clean()
        age_till_year=2022
        classid=cleaned_data['classname']
        #print(classid)
        #print(cleaned_data['student'].student_dob)
        student_date=cleaned_data['student'].student_dob
        year_obj=student_date.year
        min_age=Classes.objects.get(class_id=int(classid.class_id)).min_age
        max_age=Classes.objects.get(class_id=int(classid.class_id)).max_age
        if checking_age(age_till_year,year_obj,min_age,max_age) == True:
            raise forms.ValidationError("Student's age does not match with the class requirement")
        
    class Meta:
        model=Class_Student_Bridge
        exclude=('cs_bridgeid',)

class ClassTeachers_ModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['classname'].widget.attrs.update({'autofocus':'autofocus'})
    class Meta:
        model=Class_Teachers_Bridge
        exclude=('ct_bridgeid',)


        
