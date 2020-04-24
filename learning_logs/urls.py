from django.conf.urls import url
from . import views

urlpatterns = [
	# homepage 
	url(r'^$', views.index, name='index'),
	url(r'^topics/$', views.topics, name='topics'),
	url(r'^topics/(?P<topic_id>\d+)/$' , views.topic, name='topic'),
	# page for adding a new topic
	url(r'^new_topic/$', views.new_topic, name = 'new_topic'),
	# page for adding a new entry
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	# page for editing entries
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')
]