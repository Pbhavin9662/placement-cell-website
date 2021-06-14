from django.contrib import admin
from .models import *


# Register your models here.
class Student_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile')


admin.site.register(Student_Register, Student_admin)
admin.site.register(Student)
admin.site.register(Success_Story)
admin.site.register(Company)
admin.site.register(Student_Form)
admin.site.register(Company_Register)
admin.site.register(Selected_Students)
admin.site.register(Applied_Student)
admin.site.register(Add_vaccancy)

# admin
admin.site.register(Tpo_Update)
admin.site.register(Student_Update)

