# Generated by Django 4.2.4 on 2023-10-04 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0003_rename_project_id_taks_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taks',
            name='project',
        ),
    ]
