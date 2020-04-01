from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name='covid19_home'),
	path( 'connexion/', views.connexion, name="connexion" ),
	path( 'deconnexion/', views.deconnexion, name="deconnexion" ),
	path('identification/', views.identification, name='covid19_identification'),
	path('diagnostic/<int:quest>/', views.diagnostic, name='covid19_diagnostic'),
	path('results/', views.results_diag, name='covid19_results'),
	path('diagnostic/', views.diagnostic, name='covid19_diagnostic'),
	path('about/', views.about, name='covid19_about'),
	path('contact/', views.contact, name='covid19_contact'),
]