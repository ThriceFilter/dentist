from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name= "home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('gallery.html', views.gallery, name="gallery"),
    path('news.html', views.news, name="news"),
    path('services.html', views.services, name="services"),
    path('home.html', views.home, name="home"),
    path('index.html', views.index, name="home")
]
