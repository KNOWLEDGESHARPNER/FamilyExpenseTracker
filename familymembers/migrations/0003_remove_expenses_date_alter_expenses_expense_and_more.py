# Generated by Django 4.1.3 on 2023-01-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familymembers', '0002_expenses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='date',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='expense',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='purpose',
            field=models.TextField(default=None, max_length=120),
        ),
    ]
