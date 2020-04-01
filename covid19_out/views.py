from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .models import *
from .forms import *
from django.contrib.auth.models import User

def home(request):
	user = request.user
	if request.method == "POST":
		form_sugest = SugestionForm(request.POST or None)
		if form_sugest.is_valid():
			subject = form_sugest.cleaned_data['subject']
			if user.is_authenticated:
				Sugestion(user = user, subject=subject).save()
			return redirect(connexion)
	form_sugest = SugestionForm()
	chart = CovidChart.objects.all()

	return render(request, 'index.html', locals())

def identification(request):
	form = InscriptionForm(request.POST, request.FILES)
	if request.method == "POST" :
		if form.is_valid():
			username = form.cleaned_data['username']
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			password = form.cleaned_data['password']
			password2 = form.cleaned_data['password2']
			email = form.cleaned_data['email']
			if password==password2:
				user = User.objects.create_user(
					username=username,
					email=email,
					password=password)
				user.first_name, user.last_name = firstname, lastname
				user.save()
				print(user)
		if user:
			login(request, user)
			return redirect(diagnostic)
	form = InscriptionForm()
	return render(request, 'identification.html', locals())

def connexion(request):
	form_connection = ConnexionForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST" and form_connection.is_valid():
		username = form_connection.cleaned_data['username']
		password = form_connection.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			if next_p:
				return redirect(next_p)
			else:
				return redirect(home)
	form_connection = ConnexionForm()
	return render(request, 'connect.html', locals())

def deconnexion(request):
	logout(request)
	return redirect(home)

@login_required()
def diagnostic(request, quest=1):
	user = request.user
	questions = Questions.objects.all()
	p = Paginator(questions, 1)
	
	try:
		pagination = p.page(quest)
		question = pagination.object_list[0]
	except Exception as e:
		return redirect(results_diag)

	form = DiagnosticForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			oui = form.cleaned_data['oui']
			non = form.cleaned_data['non']
			try:
				result = get_object_or_404(Diagnostic, user=user, question=question)
				result.oui = oui
				result.non = non
				result.save()
			except Exception as e:
				Diagnostic(user = request.user, question = question, oui=oui, non=non).save()
			quest += 1
	form = DiagnosticForm()
	return render(request, 'diagnostic.html', locals())


def somme_liste(liste):
	somme = 0
	longueur = len(liste)
	for i in range(longueur):
		somme = somme + liste[i]

	return somme

def results_diag(request):
	results = Diagnostic.objects.filter(user=request.user.id)
	max_ranges = []
	margin = []
	for x in Questions.objects.all():
		max_ranges.append(x.facteur)

	max_range = somme_liste(max_ranges)*2

	for result in results:
		if result.oui == True:
			margin.append(2*result.question.facteur)
		if result.non == True:
			margin.append(0*result.question.facteur)

	final_result = somme_liste(margin)

	max_high = (100*max_range)/100
	min_high = (80*max_range)/100

	max_medium = (79*max_range)/100
	min_medium = (50*max_range)/100

	max_low = (49*max_range)/100

	print(final_result)



	return render(request, 'results.html', locals())



def about(request):
	
	return render(request, 'about.html')

def contact(request):
	user = request.user
	form_contact = ContactForm(request.POST or None)
	if request.method == 'POST':
		if form_contact.is_valid():
			full_name = form_contact.cleaned_data['full_name']
			mail = form_contact.cleaned_data['mail']
			message = form_contact.cleaned_data['message']
			if user.is_authenticated:
				ContactUs(user = user, full_name = full_name, mail=mail, message=message).save()
			return redirect(connexion)
	form_contact = ContactForm()

	return render(request, 'contact.html', locals())
