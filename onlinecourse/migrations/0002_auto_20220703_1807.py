# Generated by Django 3.1.3 on 2022-07-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(null=True),
        ),
    ]
