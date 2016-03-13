from django.shortcuts import render, redirect
from django.contrib import messages
from forms import StudentModelForm
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


def create(request):
    form = StudentModelForm()
    if request.method == 'POST':
        model = StudentModelForm(request.POST)
        if model.is_valid():
            student = model.save()
            messages.success(request, "Student %s %s has been successfully added." % (
                student.name,
                student.surname
            ))
            return redirect('students:list_view')
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    student = Student.objects.filter(pk=pk)
    if len(student) > 0:
        student = student[0]
        if request.method == 'POST':
            form = StudentModelForm(request.POST, instance=student)
            if form.is_valid():
                student = form.save()
                messages.success(request, "Info on the student has been sucessfully changed.")
        form = StudentModelForm(instance=student)
    else:
        form = ''
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    form = ''
    student = Student.objects.filter(pk=pk)
    if len(student) > 0:
        student = student[0]
        if request.method == 'POST':
            messages.success(request, "Info on %s %s has been sucessfully deleted." % (
                student.name,
                student.surname
            ))
            student.delete()
            return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
