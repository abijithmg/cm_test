from django.forms import ModelForm
from .models import Mentor, Student


class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ['id', 'name', 'expertise']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'name', 'skill_to_learn']
