# Generated by Django 4.2.4 on 2023-10-04 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_taks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taks',
            old_name='project_id',
            new_name='project',
        ),
    ]
