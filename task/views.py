# Create your views here.
from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime
from registration.models import RegistrationProfile

from django.utils import timezone
from django.contrib.auth.models import User
from task.models import Projects, Task, Goal, TaskComments
from task.forms import TaskCommentsForm


@login_required(login_url='/accounts/login/')
def home(request):
    projects = Projects.objects.all()
    users = RegistrationProfile.objects.all()
    get_tasks = Task.objects.filter(user=request.user)
    print users
    return render(request, "task/display.html", {'projects':projects, 'users':users, 'get_tasks': get_tasks })


def getproject(request):
    print "Here gethome"
    projects = Projects.objects.all()
    users = RegistrationProfile.objects.all()
    html = render_to_string("task/gethome.html", {'projects':projects, 'users':users })
    return HttpResponse(html)

@csrf_exempt
def project_task(request, project_id):
    print "Inside"
    print project_id
    users = RegistrationProfile.objects.all()
    project = Projects.objects.get(id=int(project_id))
    tasks = Task.objects.filter(project = project).filter(completed=False).order_by('-created')
    print tasks
    for t in tasks:
        comments = TaskComments.objects.filter(task=t)
        t.comments = comments
    html = render_to_string('task/project_task.html',{'project':project, 'tasks':tasks, 'users':users })
    return HttpResponse(html)

def get_goals(request, project_id):
    print "Inside get goals"
    id = project_id
    project = Projects.objects.get(id=int(id))
    #tasks = Task.objects.filter(project = project)
    goals = Goal.objects.filter(project=project)
    html = render_to_string('task/get_goals.html',{'project':project, 'goals':goals})
    return HttpResponse(html)

@csrf_exempt
def assign_to(request):
    print "Inside assign to"
    taskid = request.POST['task_id']
    user_name = request.POST['user_name']
    getuser = User.objects.get(username=user_name)
    print getuser
    task1 = Task.objects.get(id=int(taskid))
    print task1
    task1.assigned_to = getuser
    task1.save()
    pid = task1.project.id
    print pid
    users = RegistrationProfile.objects.all()
    tasks = Task.objects.filter(project = pid).filter(completed=False)
    html = render_to_string('task/project_task.html',{'tasks':tasks, 'users':users })
    return HttpResponse(html)


@csrf_exempt
def savecomments(request):
    print "inside Save Comments"
    task_id = request.POST['task_id']
    print task_id
    comments = request.POST['comments']
    pulltask = Task.objects.get(id=int(task_id))
    commentobj = TaskComments(user=request.user, task=pulltask, tcomments=comments, timestamp=timezone.now())
    commentobj.save()
    html = render_to_string('task/comment.html',{'users':request.user })
    return HttpResponse(html)
    

'''
#smaindate = changedata(sdate)
    #print smaindate
    #emaindate = changedata(edate)
    #print emaindate
    #date_object = datetime.strptime('6 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    #print date_object
    #date_objects = datetime.strptime(smaindate, '%b %d %Y %I:%M%p')
    #print date_objects
    #date_objecte = datetime.strptime(emaindate, '%b %d %Y %I:%M%p')
    #print date_objecte
'''



@csrf_exempt
def savetask(request):
    print "Inside task creation"
    pid = request.POST['data1']
    task = request.POST['task']
    task_desc = request.POST['task_desc']
    sdate = request.POST['sdate']
    edate = request.POST['edate']
    assignee = request.POST['assigne']
    user = request.user
    get_project = Projects.objects.get(id=int(pid))
    get_assignee = User.objects.get(username=assignee)
    create_task = Task(project=get_project, user=user, task=task, task_desc=task_desc, completed=False, start_date=sdate, end_date=edate, assigned_to=get_assignee, created=timezone.now())
    create_task.save()
    response = { 'message': 'Task Saved' }
    return HttpResponse(response)

'''def changedata(date):
    d = date.split('/')
    all_months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    month = d[1]
    get_month = all_months[int(d[1]-1)]
    print get_month
    get = d[2]
    byspace = get.split(" ")
    year = d[0]
    time = byspace[1]
    hours = time.split(':')
    if int(hours[0])>=12:
        print "true"
        hours=int(hours[0])-12
        final_time = str(hours)+':00PM'
        finalsdate = get_month+ " "+ byspace[0]+ " "+year + " "+final_time
    else:
        final_time=time+"AM"
        finalsdate = get_month+ " "+ byspace[0]+ " "+year + " "+final_time
    return finalsdate
'''


@csrf_exempt
def user_task(request):
    print " Inside user task"
    users = RegistrationProfile.objects.all()
    tasks = Task.objects.filter(user = request.user).filter(completed=False).order_by('-created')
    for t in tasks:
        comments = TaskComments.objects.filter(task=t)
        t.comments = comments
    html = render_to_string('task/user_task.html',{'tasks':tasks, 'users':users })
    return HttpResponse(html)

@csrf_exempt
def complete_task(request):
    print "Inside Complete Task"
    idtask = request.POST['task_id']
    tasks = Task.objects.get(id = int(idtask))
    tasks.completed = True
    tasks.save()
    html = {'message': 'Completed task'}
    return HttpResponse(html)

def logout(request):
    print "you are logged out"
    auth.logout(request)  
    messages.success(request,'Logged out successfully')
    return HttpResponseRedirect('/accounts/login/')
@csrf_exempt
def addproject(request):
    print "Inside Project creation" 
    title = request.POST['title']
    desc = request.POST['desc']
    sdate = request.POST['sdate']
    edate = request.POST['edate']
    duration = request.POST['duration']
    print sdate
    user = request.user
    create_project = Projects(user=user, project_title=title, project_description=desc, duration=duration, start_date=sdate, end_date=edate)
    create_project.save()
    print "Project Saved"
    html = "True"
    return HttpResponse(html)
    
