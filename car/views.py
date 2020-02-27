from django.shortcuts import render
from django.http import HttpResponse
from car.models import Car
# Create your views here.

def car_list(request):
	cars = Car.objects.all()
	# return HttpResponse('salem world!')
	return render(request, 'car/car_list.html', {'cars': cars})

def lexus_list(request):
	lexus = Car.objects.filter(name_auto = 'Lexus')
	# return HttpResponse('salem world!')
	return render(request, 'car/car_list.html', {'lexus': lexus})
