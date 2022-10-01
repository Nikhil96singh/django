from django.conf.urls import url
from todo.views import todolist,todoadd,contact,about,service,tododelete,todoedit



urlpatterns=[
    url(r'^$',todolist,name='todolist'),
    url(r'^add/$',todoadd,name='todoadd'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^services/$',service,name='service'),
    url(r'^about/$',about,name='about'),
    url(r'^edit/(?P<pk>\d+)/$',todoedit,name='todoedit'),
    url(r'^delete/(?P<pk>\d+)/$',tododelete,name='tododelete'),
]