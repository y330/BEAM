from django.urls import path
from . import views

urlpatterns = [
     path('imgrec', views.imgrec,name='imgrec'),
]