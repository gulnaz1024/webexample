#from django.conf.urls import url
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    #url(r'^$', views.index, name='index'),

]