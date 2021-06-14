from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        # exclude = ['user']


class StudentForms(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['user']


class CreateUserForm(UserCreationForm):
    USER = (('student', 'student'), ('company', 'company'))
    enrollment = forms.ChoiceField(required=True, choices=USER)

    class Meta:
        model = User
        fields = ['enrollment', 'username', 'email', 'password1', 'password2']


class StudentForm(ModelForm):
    class Meta:
        model = Student_Form
        fields = '__all__'


class VaccancyForm(ModelForm):
    class Meta:
        model = Add_vaccancy
        fields = '__all__'


class ApplyJobForm(ModelForm):
    class Meta:
        model = Applied_Student
        fields = '__all__'


class SuceessStoryForm(forms.ModelForm):
    class Meta:
        model = Success_Story
        fields = ['name', 'title', 'video', 'motivate_notes']
