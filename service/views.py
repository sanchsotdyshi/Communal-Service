from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from service.models import House, Aplication, Worker

def error(request, code):
	"""Error handling page"""

	template = loader.get_template('service/error.html')
	if code == 5054:
		context = {
			'text': 'Неправильный логин или пароль!',
		}
	elif code == 5088:
		context = {
			'text': 'Все поля должны быть заполнены!',
		}
	else:
		context = {
			'text': 'Неизвестная ошибка!'
		}
		
	return HttpResponse(template.render(context, request))


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
	if request.POST['house number'] == 'Номер дома' or request.POST['name'] == '' or request.POST['phone number'] == '' or request.POST['problem'] == '':
	   return HttpResponseRedirect(reverse('service:error', args=(5088,)))

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

def worker_page(request, mode=0, id=0):
	"""loads the worker page"""
	"""if mode 1 we find worker by id"""
	if mode:
		worker = Worker.objects.get(id = id)
	else:
		#Tries to find a worker with the given username and password
		try:
			worker = Worker.objects.get(login=request.POST['login'],
									password=request.POST['password'])

		#if gets an error redirects to the error page
		except Worker.DoesNotExist:
			return HttpResponseRedirect(reverse('service:error', args=(5054,)))
		
		
	aplications = Aplication.objects.filter(worker=worker, completed=0)
	template = loader.get_template('service/worker_page.html')
	context = {
		'worker': worker,
		'aplications': aplications,
	}

	return HttpResponse(template.render(context, request))

def complete_app(request, id, worker_id):
	"""Complete the application"""

	app = Aplication.objects.get(id=id)
	app.completed = 1
	app.save()
	return HttpResponseRedirect(reverse('service:worker_page', args=(1, worker_id)))
		
