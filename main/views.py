from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

import json

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.db import IntegrityError

# Create your views here.

from main.models import Manufacturer, Cereal

from main.forms import CreateCereal, CerealSearch, UserSignup, UserLogin


def initial_view(request):

	mans = Manufacturer.objects.all()
	search_form = """
		<form action="/cereal_search/" method="POST">
			<input type="text" name="name"/>

			<input type="submit" value="Submit me!"/>
		</form>
	"""
	msg = "<table>"

	for man in mans:

		manufacturer = man.name
		for cereal in man.cereal_set.all():
			facts = cereal.nutritionfacts

			name = cereal.name
			calories = facts.calories
			protein = facts.protein
			carbs = facts.carbs
			fat = facts.fat


			msg += '<tr><td>"%s"</td>' % name
			# msg += '<td>has "%s" calories</td>' % calories
			# msg += '<td>proten: %sg</td>' % protein
			# msg += '<td>carbs: %sg</td>' % carbs
			# msg += '<td>fat: %sg</td>' % fat
			for value in facts.list():
				msg += '<td>%s</td>' % value
			msg += '</tr>'
	msg += "</table>"
	return HttpResponse(msg)

@csrf_exempt
def cereal_search(request):
	mans = Manufacturer.objects.all()
	name = request.POST.get("name")
	context = {}
	for man in mans:
		for cereal in man.cereal_set.all():
			if cereal.name == name:
				context['manufacturers'] = man

	print context
	return render_to_response('base.html', context, context_instance=RequestContext(request))


def get_manufacturer_search(request):

	print request.GET

	msg = ""
	manufacturer = request.GET.get('man')
	man = Manufacturer.objects.get(name__istartswith=manufacturer)
	msg += man.name
	return HttpResponse(msg)

def post_manufacturer_search(request):
	search_form = """
		<form action="/actual_post_manufacturer_search/" method="POST">
			<input type="text" name="man"/>

			<input type="submit" value="Submit me!"/>
		</form>
	"""
	return HttpResponse(search_form)

def template_view_2(request):
	
	manufacturer_cereal = {}

	context = {}
	
	manufacturers = Manufacturer.objects.all()

	for man in manufacturers:
		cereals = man.cereal_set.filter(name__icontains="a")

		var1 = { man: cereals }

		manufacturer_cereal.update(var1)

	context['manufacturer_cereal'] = manufacturer_cereal

	return render_to_response('template_view2.html', context, context_instance=RequestContext(request))

def cereal_create(request):

	context = {}

	form = CreateCereal()
	context['form'] = form

	if request.method == 'POST':
		form = CreateCereal(request.POST)

		if form.is_valid():
			form.save()

			context['valid'] = "Cereal Saved."

	elif request.method == 'GET':
		context['valid'] = form.errors


	return render_to_response('cereal_create.html', context, context_instance=RequestContext(request))


def ajax(request):
	cereal = Cereal.objects.all()	#Gets all Cereal objects with AJAX in real time
	to_json = []
	for cereal in cereal:
		to_json.append(cereal.name)
	return_json = json.dumps(to_json)
	return HttpResponse(return_json)


def form_view(request):

	context = {}

	get = request.GET
	post = request.POST

	context['get'] = get
	context['post'] = post

	if request.method == "POST":
		cereal = request.POST.get('cereal', None)

		cereals = Cereal.objects.filter(name__istartswith=cereal)

		context['cereals'] = cereals

	elif request.method == "GET":
		context['method'] = "The method was GET"

	return render_to_response('form_view2.html', context, context_instance=RequestContext(request))

def form_view2(request):

	context = {}

	get = request.GET
	post = request.POST

	context['get'] = get
	context['post'] = post

	form = CerealSearch()

	context['form'] = form

	if request.method == "POST":
		form = CerealSearch(request.POST)

		if form.is_valid():
			cereal = form.cleaned_data['name']

			cereals = Cereal.objects.filter(name__istartswith=cereal)

			context['cereals'] = cereals
			context['valid'] = "The form was valid"
		else:
			context['valid'] = form.errors

	elif request.method == "GET":
		#context['form'] = form
		context['method'] = "The method was GET"

	return render_to_response('form_view2.html', context, context_instance=RequestContext(request))


def signup(request, registrationpage=0):

	context = {}

	form = UserSignup()
	context['form'] = form

	if request.method == 'POST':
		form = UserSignup(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			try:
				new_user = User.objects.create_user(name, email, password)
				context['valid'] = "Thank you for signing up!"

				auth_user = authenticate(username=name, password=password)
				login(request, auth_user)

				return HttpResponseRedirect('/')
			except IntegrityError, e:
				context['valid'] = "A user with that name is already taken. Please try again."

		else:
			context['valid'] = form.errors

	if request.method == 'GET':
		context['valid'] = 'Please sign up'

	return render_to_response('signup.html', context, context_instance=RequestContext(request))



#============================ good shit ======================================#



def home(request):
	context = {}

	# manus = Manufacturer.objects.all()

	# context['manus'] = manus

	return render_to_response('home.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):

	context = {}

	cereal = Cereal.objects.get(pk=pk)

	context['cereal'] = cereal

	return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))


def login_view(request):

	context = {}

	context['form'] = UserLogin()

	username = request.POST.get('username', None)
	password = request.POST.get('password', None)

	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request, user)
			context['valid'] = "Login Successful"

			HttpResponseRedirect('/home/')
		else:
			context['valid'] = "Invalid User"
	else:
		context['valid'] = "Please enter a Username"

	return render_to_response('login.html', context, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login/')


def ajax_search(request):
	context = {}

	return render_to_response('ajax_search.html', context, context_instance=RequestContext(request))

def json_response(request):
	#get string from GET dictionary
	search_string = request.GET.get('search', '')
	#filter icontains search string
	cereals = Cereal.objects.filter(name__icontains=search_string)
	#empty cereal list
	cereal_list = []
	#for loop cereals
		#append cereal names to cereal list
	for cereal in cereals:
		cereal_list.append(cereal.name)

	return JsonResponse(cereal_list, safe=False)
	#return json









#============================ testing ======================================#

def testing(request,name):
	json_list = []
	obj = Cereal.objects.filter(name__istartswith=name)
	for cereal in  obj:
		json_list.append({'cereal_name':cereal.name,"manufacturer":{"name":cereal.manufacturer.name}})
	#data = serializers.serialize('json', Cereal.objects.filter(name__istartswith=name))
	return HttpResponse(json.dumps(json_list), content_type="application/json")
	#return render_to_response('testing.html', {'manufacturers':Manufacturer.objects.all()}, context_instance=RequestContext(request))





































