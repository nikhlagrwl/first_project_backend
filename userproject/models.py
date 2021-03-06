from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from adminpanel.models import skillsList


STATUS_CHOICES = (('Applied', 'Applied'),('In Touch', 'In Touch'),('Selected', 'Selected'), ('Rejected', 'Rejected'))
# Create your models here.

# Table for the Project created
class projectInfo(models.Model):
	project_id = models.AutoField(db_column = "Project Id", primary_key = True)
	project_title = models.CharField(max_length = 100, db_column = "Project Title")
	project_description = models.CharField(max_length = 500, db_column = "Project Description")
	created_at = models.DateTimeField(auto_now_add = True, db_column = "Creation DateTime")
	project_owner = models.ForeignKey(User, db_column = "Project Owner", on_delete = models.CASCADE)
	start_date = models.CharField(max_length = 50, db_column = "Start Date", default = str(timezone.now().date()))
	end_date = models.CharField(max_length = 50, db_column = "End Date", default = str(timezone.now().date()))
	required_contributors = models.IntegerField(db_column = "Required Contributors", blank = False)


# Table for relation between project and skills required for that project
class projectSkills(models.Model):
	project_id = models.ForeignKey(projectInfo, db_column = "Project Id", on_delete = models.CASCADE)
	skill_id = models.ForeignKey(skillsList, db_column = "Skill Id", on_delete = models.CASCADE)
	status = models.BooleanField(db_column = "Status", default = True)

# Table for relation between projects and user applied to that project
class userProjectInfo(models.Model):
	user = models.ForeignKey(User, db_column = "User", on_delete = models.CASCADE, default = None)
	project = models.ForeignKey(projectInfo, db_column = "Project", on_delete = models.CASCADE, default = None)
	user_status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'Applied')