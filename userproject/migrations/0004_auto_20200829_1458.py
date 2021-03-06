# Generated by Django 3.0.8 on 2020-08-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userproject', '0003_auto_20200829_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo',
            name='end_date',
            field=models.DateField(auto_now_add=True, db_column='End Date'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='required_contributors',
            field=models.IntegerField(db_column='Required Contributors', default=1),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='start_date',
            field=models.DateField(auto_now_add=True, db_column='Start Date'),
        ),
    ]
