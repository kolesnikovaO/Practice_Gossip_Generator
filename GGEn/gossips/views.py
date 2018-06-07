from django.shortcuts import render
from . import forms
from .models import Gossip
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


"""def passwordHash(password):
    m = hashlib.md15()
    salt = "vex"
    m.update(salt.encode('utf-8') + password.encode('utf-8'))
    return m.hexdigest()"""

def about(request):
	return render(request, "AboutUs.html")

@login_required
def myprofile(request, acttype=None):
	formchangeEmail = None
	formchangeUsername = None
	formchangePasswd = None
	if acttype != None and request.method == 'POST':
		if acttype == 'changeemail':
			formchangeEmail = forms.MyProfileChangeEmailForm(request.POST)
			if formchangeEmail.is_valid():
				request.user.email = formchangeEmail.cleaned_data['new_email']
				request.user.save()
				newemail= formchangeEmail.cleaned_data['new_email']
				print("set new email to "+ newemail)
				return redirect('myprofilepattern')
		if acttype == 'changeusername':
			formchangeUsername = forms.MyProfileChangeUsernameForm(request.POST)
			if formchangeUsername.is_valid():
				request.user.username = formchangeUsername.cleaned_data['new_username']
				request.user.save()
				newusername= formchangeUsername.cleaned_data['new_username']
				print("set new username to " + newusername)
				return redirect('myprofilepattern')
		if acttype == 'changepasswd':
			formchangePasswd = forms.MyProfileChangePasswdForm(request.POST)
			if formchangePasswd.is_valid():
				oldpassword = formchangePasswd.cleaned_data['old_password']
				newpassword = formchangePasswd.cleaned_data['new_password1']
				if (request.user.check_password(oldpassword)):
					request.user.set_password(newpassword)
					request.user.save()
					print("set new password  to " + newpassword)
					return redirect('myprofilepattern')
				else:
					formchangePasswd.add_error('old_password', 'Неправильный старый пароль')


	if not formchangeEmail:
		formchangeEmail = forms.MyProfileChangeEmailForm()
		print("new formchangeEmail")
	if not formchangeUsername:
		formchangeUsername = forms.MyProfileChangeUsernameForm()
		print("new formchangeUsername")
	if not formchangePasswd:
		formchangePasswd = forms.MyProfileChangePasswdForm()
		print("new formchangePasswd")

	return render(request, 'myprofile.html', context={'formchangeEmail': formchangeEmail, 'formchangeUsername':formchangeUsername, 'formchangePasswd': formchangePasswd })


@login_required
def mystatistic(request):
	return render(request, "MyStat.html")


def home(request):
	return render(request, "create-rumour.html")


def statistic(request):
 all_gossip_num = Gossip.objects.all().count()
 available_gossip_num = Gossip.objects.filter(is_enabled=True).count()
 disappear_gossip_num = 1;

 data = { "all_gossip_num": all_gossip_num,
 "available_gossip_num": available_gossip_num,
 "disappear_gossip_num": disappear_gossip_num };

 return render(request, "statistics.html", context=data)


@login_required
def mystories(request):
	stories = Gossip.objects.filter(user_id_id=request.user.id)
	return render(request, "MyStories.html", context={ "stories": stories });
