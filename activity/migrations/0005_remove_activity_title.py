# Generated by Django 5.0.2 on 2024-05-12 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='title',
        ),
    ]
