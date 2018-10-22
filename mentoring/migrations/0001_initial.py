# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-22 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('expertise', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('skill_to_learn', models.CharField(max_length=65)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('id', 'skill_to_learn')]),
        ),
        migrations.AlterUniqueTogether(
            name='mentor',
            unique_together=set([('id', 'expertise')]),
        ),
    ]