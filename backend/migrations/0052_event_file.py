# Generated by Django 5.0.2 on 2024-03-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0051_remove_event_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='file',
            field=models.FileField(blank=True, upload_to='event_files/'),
        ),
    ]
