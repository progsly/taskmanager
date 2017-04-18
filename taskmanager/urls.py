from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
import todolist.views as views

urlpatterns = patterns('',
    url(r'^tasks/$',  views.IndexView.as_view(), name='index'),
    url(r'^tasks/create/$',  login_required(views.TaskCreate.as_view()), name='create'),
    url(r'^tasks/(?P<pk>[0-9]+)/$',  views.DetailView.as_view(), name='detail'),
    url(r'^tasks/(?P<pk>[0-9]+)/update/$',  login_required(views.TaskUpdate.as_view()), name='update'),
    url(r'^tasks/(?P<pk>[0-9]+)/delete/$',  login_required(views.TaskDelete.as_view()), name='delete'),
    url(r'^tasks/(?P<task_id>[0-9]+)/done/$',  login_required(views.mark_done), name='done'),
    url(r'^tasks/(?P<task_id>[0-9]+)/undone/$',  login_required(views.mark_undone), name='undone'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
