from django.db import models


STATUS_CHOICES = (('Applied', 'Applied'),('In Touch', 'In Touch'),('Selected', 'Selected'), ('Rejected', 'Rejected'))
# Create your models here.

# Table for the Project created
class projectInfo(models.Model):
	project_id = models.AutoField(db_column = "Project Id", primary_key = True)
	project_title = models.CharField(max_length = 100, db_column = "Project Title")
	project_description = models.CharField(max_length = 500, db_column = "Project Description")
	created_at = models.DateTimeField(auto_now_add = True, db_column = "Creation DateTime")
	project_owner = models.CharField(max_length = 150, db_column = "Project Owner")

# Table for relation between project and skills required for that project
class projectSkills(models.Model):
	project_id = models.IntegerField(db_column = "Project Id")
	skill_id = models.IntegerField(db_column = "Skill Id")

# Table for relation between projects and user applied to that project
class userProjectInfo(models.Model):
	user_id = models.CharField(max_length = 50, db_column = "User Id")
	user_status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'Applied')