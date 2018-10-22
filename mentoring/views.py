from django.shortcuts import render, redirect, get_object_or_404
from .models import Mentor, Student
from .forms import MentorForm, StudentForm


def ment_stu_list(request, template_name='ment_stu_home.html'):
    context = {}
    context['mentors'] = Mentor.objects.all()
    context['students'] = Student.objects.all()
    return render(request, template_name, context)


def mentor_create(request, template_name='mentor_form.html'):
    form = MentorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mentoring:ment_stu_list')
    return render(request, template_name, {'form': form})


def mentor_edit(request, pk, template_name='mentor_form.html'):
    mentor = get_object_or_404(Mentor, pk=pk)
    form = MentorForm(request.POST or None, instance=mentor)
    if form.is_valid():
        form.save()
        return redirect('mentoring:ment_stu_list')
    return render(request, template_name, {'form': form})


def mentor_delete(request, pk, template_name='mentor_delete.html'):
    mentor = get_object_or_404(Mentor, pk=pk)
    if request.method == 'POST':
        mentor.delete()
        return redirect('mentoring:ment_stu_list')
    return render(request, template_name, {'mentor': mentor})


def student_create(request, template_name='mentor_form.html'):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('mentoring:ment_stu_list')
    return render(request, template_name, {'form': form})


def student_edit(request, pk, template_name='mentor_form.html'):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('mentoring:ment_stu_list')
    return render(request, template_name, {'form': form})


def student_delete(request, pk, template_name='student_delete.html'):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('mentoring:ment_stu_list')
    return render(request, template_name, {'student': student})


def search_mentors(request, pk, template_name='available_mentors_list.html'):
    student = get_object_or_404(Student, pk=pk)
    mentors = Mentor.objects.filter(expertise=student.skill_to_learn)
    return render(request, template_name, {'student': student, 'mentors':mentors})