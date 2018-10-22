from django.db import models
from django.urls import reverse


class Mentor(models.Model):
    name = models.CharField(max_length=65)
    expertise = models.CharField(max_length=65)

    class Meta:
        unique_together = ("id", "expertise")

    def __str__(self):
        return self.name

    def get_post_url(self):
        return reverse('mentor_edit', kwargs={'id': self.pk})


class Student(models.Model):
    mentor = models.ManyToManyField(Mentor)
    name = models.CharField(max_length=65)
    skill_to_learn = models.CharField(max_length=65)

    class Meta:
        unique_together = ("id", "skill_to_learn")

    def __str__(self):
        return self.name

    def get_post_url(self):
        return reverse('student_edit', kwargs={'pk': self.pk})
