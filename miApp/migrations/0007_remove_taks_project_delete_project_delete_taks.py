# Generated by Django 4.2.4 on 2023-10-04 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taks',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Taks',
        ),
    ]
