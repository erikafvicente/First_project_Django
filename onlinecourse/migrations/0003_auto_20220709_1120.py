# Generated by Django 3.1.3 on 2022-07-09 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20220703_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_text',
        ),
    ]
