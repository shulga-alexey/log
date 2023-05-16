# Generated by Django 4.1.9 on 2023-05-16 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('appointor_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('status', models.CharField(choices=[('RJ', 'Rejected'), ('AC', 'Accepted')], default='RJ', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('appointor_teachers', models.ManyToManyField(related_name='appointor_tasks', through='tasks.AppointedTask', to='users.teacher')),
                ('producer_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produced_tasks', to='users.teacher')),
                ('students', models.ManyToManyField(related_name='tasks', through='tasks.AppointedTask', to='users.student')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='appointedtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
    ]
