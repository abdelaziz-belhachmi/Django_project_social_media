# Generated by Django 5.0.2 on 2024-03-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_utilisateur_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='profile_picture',
            field=models.ImageField(blank=True, default='staticfiles/Assets/Images/us2.png', upload_to='profile_pictures/'),
        ),
    ]