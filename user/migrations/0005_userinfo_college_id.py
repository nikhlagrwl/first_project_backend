# Generated by Django 3.0.8 on 2020-08-26 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_userinfo_college_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='college_id',
            field=models.IntegerField(db_column='College Id', null=True),
        ),
    ]