from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services/', views.services_list, name='services'),
    path('services/<int:id>/', views.service_detail, name='service_detail'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/<int:id>/', views.portfolio_detail, name='portfolio_detail'),
    path('testimonials/', views.all_testimonials, name='all_testimonials'),
    path('add-feedback/', views.add_feedback, name='add_feedback'),
    path('contact/', views.contact, name='contact'),


]
