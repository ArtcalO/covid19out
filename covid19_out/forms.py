from django.db import models
from django import forms
from .models import *

class DiagnosticForm(forms.ModelForm):
	oui = forms.BooleanField(widget=forms.CheckboxInput(attrs = {'id':'exemple','name':'case'}),required=False)
	non = forms.BooleanField(widget=forms.CheckboxInput(attrs = {'id':'exemple','name':'case'}),required=False)
	class Meta :
		model = Diagnostic
		exclude = ['question', 'user']

class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nom utilisateur ','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'type':'password','class':'form-control'}))

class InscriptionForm(forms.Form):
	firstname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom ','class':'form-control'}), label='nom')
	lastname = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Prenom ','class':'form-control'}), label='prenom')
	username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom utilisateur ','class':'form-control'}), label='username')
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe ','class':'form-control'}), label='password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirmer ','class':'form-control'}), label='confirm password')
	email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Adresse electronique ','class':'form-control'} ), label='your email adress')

class ContactForm(forms.Form):
	full_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom Complet','class':'form-control'}), label='nom')
	mail = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Adresse électronique ','class':'form-control'} ), label='your email adress')
	message = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Votre texte ','class':'form-control'}), label='nom')


class SugestionForm(forms.ModelForm):
	subject = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Sugestion ','class':'form-control'}), label='nom')

	class Meta:
		model = Sugestion
		exclude = ['user']

# Create your models here.
