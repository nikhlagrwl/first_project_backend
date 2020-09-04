# Generated by Django 3.0.8 on 2020-09-04 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0010_auto_20200829_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskills',
            name='skill',
            field=models.ForeignKey(db_column='Skill Name', on_delete=django.db.models.deletion.CASCADE, to='adminpanel.skillsList'),
        ),
        migrations.AlterField(
            model_name='userskills',
            name='username',
            field=models.ForeignKey(db_column='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]