from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from django.db.models import Q,Sum
# Create your views here.

def get_students(request):
    queryset = Student.objects.all()
    
    # search functionality logic
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset=queryset.filter(
            
            Q(student_name__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_address__icontains = search)| 
            Q(student_address__icontains = search)| 
            Q(student_age__icontains = search) 
        )

    paginator = Paginator(queryset, 15)  # Show 15 student per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    return render(request,'students.html',context={'queryset':page_obj})

from .seed import generate_rank

def diplay_marks(request, student_id):
    # generate_rank()
    student_id_obj = StudentId.objects.get(student_id=student_id)
    student_detail = Student.objects.get(student_id=student_id_obj)

    query_set = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks =  query_set.aggregate(total_marks=Sum('marks'))

    #  rank
    # rank=1
    # ranks=Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks')
    # for r in ranks:
    #     if student_id == r.student_id.student_id:
    #         break
    #     rank+=1

    return render(request,'display_marks.html',context={ 'student_detail':student_detail ,'queryset':query_set,'totalmarks':total_marks})
