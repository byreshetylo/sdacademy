from django.shortcuts import render
from models import Student


def detail(request, pk):
    context = {}
    student_info = Student.objects.filter(pk=pk)
    if len(student_info) > 0:
        context = {
            'student_info': student_info[0],
        }
    return render(request, 'students/detail.html', context)


def list_view(request):
    by_id = request.GET.get('course_id')
    if by_id:
        students = Student.objects.filter(courses=by_id)
    else:
        students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/list.html', context)
