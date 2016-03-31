from django.forms import ModelForm
from models import Lesson


class LessonModelForm(ModelForm):
    class Meta:
        model = Lesson
