# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-15 06:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clazz',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_no', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.SmallIntegerField(max_length=10)),
                ('sname', models.CharField(max_length=30)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu.clazz')),
                ('cour', models.ManyToManyField(to='stu.course')),
            ],
        ),
    ]
