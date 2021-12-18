from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('resume/', views.resume, name="resume"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio-single/<str:pk>', views.portfolio_single, name='portfolio-single'),
    path('service/', views.service, name="service"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name='contact'),
    path('skills/', views.skills, name='skills'),
    path('blog/', views.blog, name="blog"),
    path('blog-single/<str:pk>', views.blog_single, name="blog-single"),
]