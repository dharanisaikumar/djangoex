# Generated by Django 2.2.5 on 2020-02-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regapp', '0002_remove_usermodel_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='ppic',
        ),
    ]
