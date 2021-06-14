from __future__ import unicode_literals
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='basicpic.png', null=True, blank=True)

    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='basicpic.png', null=True, blank=True)

    # date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Student_Register(models.Model):
    enrollment = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    pwd = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Student_Form(models.Model):
    SEM = (
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    BRANCH = (
        ('IT', 'IT'),
        ('CE', 'CE'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    s_name = models.CharField(max_length=100, default='')
    s_e_num = models.CharField(max_length=100, default='')
    s_sem = models.CharField(max_length=100, null=True, choices=SEM)
    s_branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    s_gender = models.CharField(max_length=6, null=True, choices=GENDER)
    s_mobile = models.CharField(max_length=100, default='')
    s_email = models.EmailField(max_length=200, default='')
    s_ssc_per = models.CharField(max_length=30, default="")
    s_hsc_per = models.CharField(max_length=30, default="")
    s_cpi = models.CharField(max_length=10, default='10')
    s_cgpa = models.CharField(max_length=10, default='10')
    s_resume = models.FileField(validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])])
    s_profile = models.ImageField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    s_dob = models.DateTimeField(default='')
    s_address = models.TextField(max_length=300, default='')
    s_state = models.CharField(max_length=15, default='')
    s_dist = models.CharField(max_length=15, default='')
    s_pincode = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.s_name


# company models

class Company_Register(models.Model):
    name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    address = models.TextField(max_length=300, null=True)
    pwd = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Selected_Students(models.Model):
    BRANCH = (
        ('IT', 'IT'),
        ('CE', 'CE'),
    )
    SELECTED = (
        ('Selected', 'Selected'),
        ('Not Selected', 'Not Selected'),
    )
    enrollment = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=100, null=True)
    branch = models.CharField(max_length=100, null=True, choices=BRANCH)
    selected = models.CharField(max_length=20, null=True, choices=SELECTED)

    def __str__(self):
        return self.name


class Add_vaccancy(models.Model):
    job_title = models.CharField(max_length=100, null=True)
    salary = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=100, null=True)
    no_of_opening = models.CharField(max_length=100, null=True)
    apply_date = models.DateField(auto_now_add=True, null=True)
    last_date = models.DateField(default="30/02/20", help_text="(mm/dd/yyyy)")

    def __str__(self):
        return self.name


class Apply_job(models.Model):
    resume = models.FileField(upload_to='pcapp/Files/', default='')


# Admin database........

class Tpo_Update(models.Model):
    tpo_update = models.TextField(max_length=300, default='1')

    def __str__(self):
        return self.tpo_update


class Student_Update(models.Model):
    student_update = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.student_update


class Applied_Student(models.Model):
    name = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    enrollment = models.CharField(max_length=100, default="00")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    job_resume = models.FileField(validators=[FileExtensionValidator(['pdf', 'docx', 'doc'])],
                                  help_text="(pdf,docx,doc)")

    def __str__(self):
        return self.enrollment


class Success_Story(models.Model):
    name = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, default="No title")
    video = models.FileField(upload_to='video/', validators=[FileExtensionValidator(['mp4', 'm4p', 'm4v', 'MPEG'])],
                             help_text="(mp4, m4p, m4v, MPEG)")
    motivate_notes = models.TextField(max_length=400, default='Not Writes')

    def __str__(self):
        return self.title
