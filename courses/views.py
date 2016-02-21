from django.shortcuts import render
from models import Course, Lesson


def index(request):
    return render(request, 'courses/detail.html')


def detail(request, pk):
    context = {
        'course_info': Course.objects.filter(id=pk)[0],
        'lessons': Lesson.objects.filter(course=pk)
    }
    return render(request, 'courses/detail.html', context)
