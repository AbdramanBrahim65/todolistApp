# Generated by Django 3.2.8 on 2022-03-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tachemodel',
            options={'ordering': ['-date_add']},
        ),
        migrations.AlterField(
            model_name='tachemodel',
            name='date_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
