from django.conf.urls import patterns, url
from .views import IndexView ,getCoordinates, sendGrid, twilio
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getwell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   
    url(r'^$', IndexView.as_view(), name='index'),

	url(r'^getCoordinates/$', getCoordinates, name='coor'),
	url(r'^sendgrid/$', sendGrid, name='sendGrid'),
	url(r'^twilio/$', twilio, name='twilio'),
)
