# Generated by Django 3.1.3 on 2020-11-24 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('info', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('access', models.CharField(max_length=1)),
                ('office', models.CharField(max_length=20)),
                ('phoneNum', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('officeHours', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus_maker.course')),
                ('teachingAssistant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus_maker.myuser')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus_maker.myuser'),
        ),
    ]