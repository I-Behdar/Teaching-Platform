# Generated by Django 4.0.6 on 2023-03-15 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('users', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectassignment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student'),
        ),
        migrations.AddField(
            model_name='projectassignment',
            name='supervisor',
            field=models.ManyToManyField(to='users.teacher'),
        ),
        migrations.AddField(
            model_name='project',
            name='accepted_teachers',
            field=models.ManyToManyField(to='users.teacher'),
        ),
        migrations.AddField(
            model_name='project',
            name='requirements',
            field=models.ManyToManyField(to='subjects.subject'),
        ),
    ]
