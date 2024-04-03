from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(StudentId)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id','student_name','department']
admin.site.register(Student,StudentAdmin)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']
admin.site.register(SubjectMarks,SubjectMarksAdmin)