# Generated by Django 4.0.4 on 2022-05-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_completed_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed',
            name='completed',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='completed_item',
            field=models.BooleanField(default=False),
        ),
    ]