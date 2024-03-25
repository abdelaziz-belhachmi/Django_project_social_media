# Generated by Django 5.0.2 on 2024-03-24 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0055_remove_research_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='utilisateur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.utilisateur'),
            preserve_default=False,
        ),
    ]
