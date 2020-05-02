from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('contact', views.contact),
    path('details', views.details),
    path('functions', views.functions),
    path('apperance', views.apperance),
    path('pricing', views.pricing),
    
]