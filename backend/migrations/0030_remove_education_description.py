# Generated by Django 5.0.2 on 2024-03-23 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_alter_certification_nom_certificat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='description',
        ),
    ]
