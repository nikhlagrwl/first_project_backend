# Generated by Django 3.0.8 on 2020-08-27 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_userinfo_college_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='college_id',
        ),
    ]