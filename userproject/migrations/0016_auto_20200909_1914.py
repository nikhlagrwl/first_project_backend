# Generated by Django 3.0.8 on 2020-09-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userproject', '0015_auto_20200909_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='end_date',
            field=models.CharField(db_column='End Date', default='2020-09-09', max_length=50),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='start_date',
            field=models.CharField(db_column='Start Date', default='2020-09-09', max_length=50),
        ),
    ]
