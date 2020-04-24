from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.core.urlresolvers import reverse
from . models import Topic, Entry
from . forms import TopicForm, EntryForm

def index(request):
	""" the home_page for learning log"""
	return render(request, 'learning_logs/index.html')


def topics(request):
 	"""Show all topics."""
 	topics = Topic.objects.order_by('date_added')
 	context = {'topics': topics}
 	return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
	""" show a single topic and all its entries """
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
	""" allow users to create a new topic"""
	if request.method != 'POST':
		# No data submitted ; create a blank form.
		form = TopicForm()
	else:
		# post data submitted; process data
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}

	return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request,topic_id):
	""" allow users to create a new entry associated with a given topic"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# no data submitted; create a blank form
		form = EntryForm()
	else:
		# post data submitted; process data
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
	""" allow user to edit the entries that they have already added"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		# initial request; pre fill form with the current entry
		form = EntryForm(instance=entry)
	else:
		# post data submitted and process it
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)



	