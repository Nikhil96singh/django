
from django.conf.urls import url,include
from django.contrib import admin
from todo.views import home,todolist

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home, name='home'),
    url(r'^todos/$',todolist, name='todolist'),
    url(r'^todos/',include('todo.urls',namespace='todo')),
    url(r'^acc/',include('account.urls')),
]


