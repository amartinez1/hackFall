from django.conf.urls import patterns, include, url
from .views import IndexView ,getCoordinates
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getwell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   
    url(r'^$', IndexView.as_view(), name='index'),

	url(r'^getCoordinates/$', getCoordinates, name='coor'),
)
