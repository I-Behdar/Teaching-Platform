# Generated by Django 4.0.6 on 2023-02-14 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lesson_type',
            field=models.CharField(choices=[('B', 'Backend'), ('F', 'Frontend'), ('D', 'Devops'), ('S', 'System Administration'), ('C', 'Cloud Engineering')], max_length=1),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='specialization',
            field=models.CharField(choices=[('B', 'Backend'), ('F', 'Frontend'), ('D', 'Devops'), ('S', 'System Administration'), ('C', 'Cloud Engineering')], max_length=128),
        ),
    ]
