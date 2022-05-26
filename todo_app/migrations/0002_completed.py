# Generated by Django 4.0.4 on 2022-05-26 16:38

from django.db import migrations, models
import django.db.models.deletion
import todo_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_date', models.DateTimeField(default=todo_app.models.one_week_hence)),
                ('todo_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.todoitem')),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo_app.todolist')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]