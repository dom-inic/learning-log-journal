from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def logout_view(request):
	""" log the user out"""
	logout(request)
	return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
	""" register a new user"""
	if request.method != 'POST':
		# display blank registration form
		form = UserCreationForm()
	else:
		# process completed form
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			# log the user in and then redirect to homepage
			authenticated_user = authenticate(username=new_user.username,
				password=request.POST['password']
				)
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)
