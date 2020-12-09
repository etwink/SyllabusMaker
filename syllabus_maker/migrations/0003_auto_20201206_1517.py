# Generated by Django 3.1.3 on 2020-12-06 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_maker', '0002_auto_20201206_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabus_maker.section'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='office',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='officeHours',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phoneNum',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='syllabus_maker.myuser'),
        ),
    ]
