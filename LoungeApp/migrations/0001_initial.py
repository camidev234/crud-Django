# Generated by Django 4.2.4 on 2023-10-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lounge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lounge_number', models.CharField(max_length=100)),
                ('lounge_description', models.CharField(max_length=300)),
                ('lounge_students', models.IntegerField()),
            ],
        ),
    ]
