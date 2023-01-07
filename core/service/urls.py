from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda/', views.about, name='about'),
    path('siparisal/', views.service_form, name='service_form'),
    path('iletisim/', views.contact, name='contact'),
    path('giris/', views.log_in, name='login'),
    path('home/', views.home, name='home'),
]
