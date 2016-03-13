from django.shortcuts import render, redirect
from models import Course, Lesson
from forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def index(request):
    return render(request, 'courses/detail.html')


def detail(request, pk):
    context = {
        'course_info': Course.objects.filter(id=pk)[0],
        'lessons': Lesson.objects.filter(course=pk),
    }
    return render(request, 'courses/detail.html', context)


def add(request):
    form = CourseModelForm()
    if request.method == 'POST':
        model = CourseModelForm(request.POST)
        if model.is_valid():
            course = model.save()
            messages.success(request, "Course %s has been successfully added." % course.name)
            return redirect('index')
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    course = Course.objects.filter(pk=pk)
    if len(course) > 0:
        course = course[0]
        if request.method == 'POST':
            form = CourseModelForm(request.POST, instance=course)
            if form.is_valid():
                course = form.save()
                messages.success(request, "The changes have been saved.")
        form = CourseModelForm(instance=course)
    else:
        form = ''
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    form = ''
    course = Course.objects.filter(pk=pk)
    if len(course) > 0:
        course = course[0]
        if request.method == 'POST':
            messages.success(request, "Course %s has been deleted." % course.name)
            course.delete()
            return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    form = LessonModelForm(initial={'course': pk})
    if request.method == 'POST':
        model = LessonModelForm(request.POST)
        if model.is_valid():
            lesson = model.save()
            messages.success(request, "Lesson %s has been successfully added." % lesson.subject)
            return redirect('courses:detail', pk=pk)
    return render(request, 'courses/add_lesson.html', {'form': form})
