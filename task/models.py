from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Projects(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    project_title = models.CharField(max_length=200)
    project_description = models.CharField(max_length=3000)
    duration = models.CharField(max_length=100, null=True, blank=True)
    project_creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.project_title
    
    
class Task(models.Model):
    project = models.ForeignKey(Projects, blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True,  related_name='user_created')
    task = models.CharField(max_length=500)
    task_desc = models.CharField(max_length=3000, null=True, blank=True)
    completed = models.BooleanField(default=False)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, null=True, blank=True,  related_name='user_assignedto')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __unicode__(self):
        return self.task



class TaskComments(models.Model):
    task = models.ForeignKey(Task, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    tcomments = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __unicode__(self):
        return self.tcomments
  
class Goal(models.Model):
    project = models.ForeignKey(Projects, null=True, blank=True)
    goal_title = models.CharField(max_length=300, null=True, blank=True)
    goal_desc = models.CharField(max_length=3000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True) 
    
    def __unicode__(self):
        return self.goal_title