# Generated by Django 3.0.8 on 2020-08-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userproject', '0002_auto_20200829_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='end_date',
            field=models.DateField(db_column='End Date', default=None),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='start_date',
            field=models.DateField(db_column='Start Date', default=None),
        ),
    ]