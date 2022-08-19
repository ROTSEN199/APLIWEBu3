from django.urls import path
from catstudent import views
from django.views.generic.base import TemplateView # new
 
urlpatterns = [
   path("", views.index, name="index"),
]

