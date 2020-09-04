# Generated by Django 3.0.8 on 2020-08-26 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='college_name',
            field=models.CharField(db_column='College Name', default='Guru', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='country',
            field=models.CharField(db_column='Country', default='India', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='state',
            field=models.CharField(db_column='State', default='India', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.OneToOneField(db_column='User', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]