from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from models import Student
from sdacademy.utils import MyCustomTitleMixin


class StudentListView(ListView):
    model = Student
    paginate_by = 2

    def get_queryset(self):
        by_id = self.request.GET.get('course_id')
        if by_id:
            students = Student.objects.filter(courses=by_id)
        else:
            students = Student.objects.all()
        return students


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(MyCustomTitleMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    custom_title = 'Student registration'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Student %s %s has been successfully added." % (
                self.object.name,
                self.object.surname
            ))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(MyCustomTitleMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:edit')
    custom_title = 'Student info update'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Info on the student has been sucessfully changed.")
        return self.render_to_response(self.get_context_data(form=form))


class StudentDeleteView(MyCustomTitleMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    custom_title = 'Student info suppression'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, "Info on %s %s has been sucessfully deleted." % (
                self.object.name,
                self.object.surname
            ))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)
