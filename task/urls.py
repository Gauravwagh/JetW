from django.conf.urls import patterns, url

urlpatterns = patterns('task.views',
                        url(r'^project_task/(?P<project_id>\d+)$', 'project_task'),
                        url(r'^get_goals/(?P<project_id>\d+)$', 'get_goals'),
                        url(r'^assign_to/$', 'assign_to'),
                        url(r'^getproject/$', 'getproject'),
                        url(r'^savecomments/$', 'savecomments'),
                        url(r'^savetask/$', 'savetask'),
                        url(r'^addproject/$', 'addproject'),
                        url(r'^user_task/$', 'user_task'),
                        url(r'^complete_task/$', 'complete_task'),
                        url(r'^logout/$', 'logout'),
   

                       )