from django.contrib import admin

from task.models import Task, TaskComments, Goal, Projects


    
admin.site.register(Task)
admin.site.register(TaskComments)
admin.site.register(Goal)
admin.site.register(Projects)