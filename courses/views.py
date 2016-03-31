from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Course, Lesson
from forms import LessonModelForm
from sdacademy.utils import MyCustomTitleMixin


class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course=self.object.pk)
        return context


class CourseCreateView(MyCustomTitleMixin, CreateView):
    model = Course
    # success_url = reverse_lazy('index')  # moved to model
    custom_title = 'Course creation'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Course %s has been successfully added." % self.object.name)
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(MyCustomTitleMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('Courses:edit')
    custom_title = 'Course update'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "The changes have been saved.")
        return self.render_to_response(self.get_context_data(form=form))


class CourseDeleteView(MyCustomTitleMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    custom_title = 'Course deletion'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, "Course %s has been deleted." % self.object.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


def add_lesson(request, pk):
    form = LessonModelForm(initial={'course': pk})
    if request.method == 'POST':
        model = LessonModelForm(request.POST)
        if model.is_valid():
            lesson = model.save()
            messages.success(request, "Lesson %s has been successfully added." % lesson.subject)
            return redirect('courses:detail', pk=pk)
    return render(request, 'courses/add_lesson.html', {'form': form})
