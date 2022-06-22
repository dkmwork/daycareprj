from django.db import models
import re
from django.core.exceptions import ValidationError

def validate_email(value):
    rule=re.compile("^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$")
    if not rule.match(value):
        raise ValidationError(f"{value} is not a valid email address")


def validate_mobileno(value):
        rule=re.compile("^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$")
        if not rule.match(value):
            raise ValidationError(f"{value} is not a valid mobile number")

class Classes(models.Model):
    class_id=models.IntegerField(primary_key=True,auto_created=True)
    class_name=models.CharField(max_length=40,null=False,blank=False,unique=True)
    min_age=models.IntegerField(null=False,blank=False)
    max_age=models.IntegerField(null=False,blank=False)
    max_student=models.IntegerField(null=False,blank=False)
    class_fee=models.IntegerField(null=False,blank=False)
    def __str__(self):
        return self.class_name
class Student(models.Model):
    student_id=models.IntegerField(primary_key=True,auto_created=True)
    gender=(("Female","Female"),("Male","Male"))
    student_name=models.CharField(max_length=40,null=False,blank=False)
    student_dob=models.DateField(null=True,blank=True,verbose_name="Date of Birth")
    student_class=models.ForeignKey(Classes,on_delete=models.PROTECT,null=True,blank=True,related_name='student')
    student_gender=models.CharField(max_length=10,choices=gender,verbose_name='Gender')
    guardian_name=models.CharField(max_length=40,null=False,blank=False)
    contact_no=models.CharField(validators=[validate_mobileno],max_length=20,unique=True,null=False,blank=False,verbose_name="Contact Number")
    student_email=models.CharField(validators=[validate_email],max_length=40,unique=True,null=True,blank=True)
    def __str__(self):
        return self.student_name
class Qualification(models.Model):
    quali_id=models.IntegerField(primary_key=True,auto_created=True)
    qualification=models.CharField(max_length=100,null=False,blank=False)
    quali_code=models.CharField(max_length=10,null=False,blank=False,unique=True)
    def __str__(self):
        return self.qualification
class Teachers(models.Model):
    teacher_id=models.IntegerField(primary_key=True,auto_created=True)
    teacher_name=models.CharField(max_length=40,null=False,blank=False)
    contact_no=models.CharField(validators=[validate_mobileno],max_length=20,unique=True,null=False,blank=False,verbose_name="Contact Number")
    teachers_email=models.CharField(validators=[validate_email],max_length=40,unique=True,null=True,blank=True)
    qualifications=models.ForeignKey(Qualification,on_delete=models.PROTECT,null=True,blank=True,related_name="teachers")
    years_experience=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.teacher_name
class Teacher_Qualification_Bridge(models.Model):
    tq_bridgeid=models.IntegerField(primary_key=True,auto_created=True)
    teacher=models.ForeignKey(Teachers,on_delete=models.PROTECT,null=True,blank=True,related_name="teacher_qualification_bridge")
    qualification=models.ForeignKey(Qualification,on_delete=models.PROTECT,null=True,blank=True,related_name="teacher_qualification_bridge")
    def __str__(self):
        return self.teacher

class Class_Student_Bridge(models.Model):
    cs_bridgeid=models.IntegerField(primary_key=True,auto_created=True)
    classname=models.ForeignKey(Classes,on_delete=models.PROTECT,null=True,blank=True,related_name="class_student_bridge")
    student=models.ForeignKey(Student,on_delete=models.PROTECT,null=True,blank=True,related_name="class_student_bridge")
    def __str__(self):
        return f"{self.student} {self.classname}"
class Class_Teachers_Bridge(models.Model):
    ct_bridgeid=models.IntegerField(primary_key=True,auto_created=True)
    classname=models.ForeignKey(Classes,on_delete=models.PROTECT,null=True,blank=True,related_name="class_teacher_bridge")
    teacher=models.ForeignKey(Teachers,on_delete=models.PROTECT,null=True,blank=True,related_name="class_teacher_bridge")
    def __str__(self):
        return f"{self.teacher} {self.classname}"







# Create your models here.
