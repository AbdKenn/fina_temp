# Generated by Django 3.1.3 on 2021-05-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_mark',
            field=models.IntegerField(default=0),
        ),
    ]
