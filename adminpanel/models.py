from django.db import models


# TIER_LIST = (('Tier I', 'Tier I'), ('Tier II', 'Tier II'), ('Tier III', 'Tier III'))

# Create your models here.

class collegeList(models.Model):
	college_id = models.AutoField(primary_key = True, db_column = "College Id")
	college_name = models.CharField(max_length = 100, db_column = "College Name")
	college_city = models.CharField(max_length = 50, db_column = "College City")
	# college_tier = models.CharField(max_length = 10, db_column = "Tier", choices = TIER_LIST)

class skillsList(models.Model):
	skill_id = models.AutoField(primary_key = True, db_column = "Skill Id")
	skill_name = models.CharField(max_length = 30, db_column = "Skill Name")