# Generated by Django 3.0.8 on 2020-09-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userproject', '0008_auto_20200904_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectskills',
            name='status',
            field=models.CharField(db_column='Status', default=1, max_length=2),
        ),
    ]
