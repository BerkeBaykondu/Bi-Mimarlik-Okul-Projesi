# Generated by Django 3.1.5 on 2021-01-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projects_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='title',
        ),
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/project'),
        ),
    ]
