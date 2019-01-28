# Generated by Django 2.1.5 on 2019-01-28 11:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='times',
        ),
        migrations.AddField(
            model_name='time',
            name='task',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
            preserve_default=False,
        ),
    ]
