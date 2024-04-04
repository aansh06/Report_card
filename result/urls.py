from django.urls import path
from .views import *

urlpatterns = [
    path('',get_students,name='get_students'),
    path('marks/<student_id>',diplay_marks,name='marks')
]