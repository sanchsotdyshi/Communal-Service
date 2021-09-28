from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from service.models import House, Aplication, Worker
# Create your views here.

def main(request):
	"""loads main page"""

	template = loader.get_template('service/main.html')
	houses = House.objects.all()
	context = {
		'houses': houses,
	}
	return HttpResponse(template.render(context, request))

def create_application(request):
	"""Create new application and
	 redirect to main page"""

	house = House.objects.get(id=request.POST['house number'])
	worker = house.worker
	new_application = Aplication(name=request.POST['name'],
								 phone_number=request.POST['phone number'],
								 house_number=house.number,
								 problem=request.POST['problem'],
								 worker=worker)
	new_application.save()
	return HttpResponseRedirect(reverse('service:main'))

def login(request):
	"""loads the workers login page"""

	template = loader.get_template('service/login.html')
	return HttpResponse(template.render({}, request))

def worker_page(request):
	"""loads the worker page"""

	#Tries to find a worker with the given username and password
	try:
		worker = Worker.objects.get(login=request.POST['login'],
									password=request.POST['password'])

	#if gets an error redirects to the error page
	except Worker.DoesNotExist:
		template = loader.get_template('service/error.html')
		context = {
			'text': 'Неправильный логин или пароль!',
		}
	#else load page
	else:
		aplications = Aplication.objects.filter(worker=worker)
		template = loader.get_template('service/worker_page.html')
		context = {
			'worker': worker,
			'aplications': aplications,
		}
		
	return HttpResponse(template.render(context, request))
	
		
