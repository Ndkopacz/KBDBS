from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.
#def post_list(request):
#    return render(request, 'blog/post_list.html', {})

def post_list(request):
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			name = form.cleaned_data['name']
			recipients = ['KBDBS.LLC@gmail.com']
			
			fullMessage = "From: " + sender + "\nName: " + name + "\n\nMessage: " + message
			send_mail("Message through Website", fullMessage, sender, recipients)

			return HttpResponseRedirect('/')
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()

	return render(request, 'blog/post_list.html', {'form': form})
	
