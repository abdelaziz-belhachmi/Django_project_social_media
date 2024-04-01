# Generated by Django 5.0.3 on 2024-04-01 13:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0069_rename_creator_postclassroom_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qcm',
            old_name='Classroom',
            new_name='QCMClassroom',
        ),
        migrations.RenameField(
            model_name='qcm',
            old_name='delai',
            new_name='QCMdelai',
        ),
        migrations.RenameField(
            model_name='qcm',
            old_name='description',
            new_name='QCMdescription',
        ),
        migrations.RenameField(
            model_name='qcm',
            old_name='title',
            new_name='QCMtitle',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='fileTask',
            field=models.FileField(blank=True, upload_to='task_files/'),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='studentQcmfinished',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qcm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.qcm')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='TaskResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_Response', models.FileField(upload_to='task_responses/')),
                ('submission_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.etudiant')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.task')),
            ],
        ),
    ]
