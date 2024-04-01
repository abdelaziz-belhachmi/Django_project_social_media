# Generated by Django 5.0.2 on 2024-03-29 19:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0065_classroomparticipants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qcm',
            name='professor',
        ),
        migrations.AddField(
            model_name='qcm',
            name='Classroom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.classroom'),
        ),
        migrations.AddField(
            model_name='qcm',
            name='delai',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qcm',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]