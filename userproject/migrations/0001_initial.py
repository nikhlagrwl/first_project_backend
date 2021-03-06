# Generated by Django 3.0.8 on 2020-08-29 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectInfo',
            fields=[
                ('project_id', models.AutoField(db_column='Project Id', primary_key=True, serialize=False)),
                ('project_title', models.CharField(db_column='Project Title', max_length=100)),
                ('project_description', models.CharField(db_column='Project Description', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='Creation DateTime')),
                ('project_owner', models.OneToOneField(db_column='Project Owner', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.CharField(choices=[('Applied', 'Applied'), ('In Touch', 'In Touch'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], default='Applied', max_length=20)),
                ('project_id', models.OneToOneField(db_column='Project Id', on_delete=django.db.models.deletion.CASCADE, to='userproject.projectInfo')),
                ('username', models.OneToOneField(db_column='Username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='projectSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.OneToOneField(db_column='Project Id', on_delete=django.db.models.deletion.CASCADE, to='userproject.projectInfo')),
                ('skill_id', models.OneToOneField(db_column='Skill Id', on_delete=django.db.models.deletion.CASCADE, to='adminpanel.skillsList')),
            ],
        ),
    ]
