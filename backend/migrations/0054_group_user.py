# Generated by Django 5.0.2 on 2024-03-24 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0053_remove_group_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin_groups', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]