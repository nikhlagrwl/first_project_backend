# Generated by Django 3.0.8 on 2020-08-29 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userproject', '0005_auto_20200829_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectskills',
            name='project_id',
            field=models.ForeignKey(db_column='Project Id', on_delete=django.db.models.deletion.CASCADE, to='userproject.projectInfo'),
        ),
    ]
