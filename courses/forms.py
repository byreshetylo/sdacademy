from django.forms import ModelForm
from models import Lesson, Course


class CourseModelForm(ModelForm):
    class Meta:
        model = Course


class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson