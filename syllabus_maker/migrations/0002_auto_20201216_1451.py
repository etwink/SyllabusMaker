# Generated by Django 3.1.3 on 2020-12-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_maker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='department',
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
