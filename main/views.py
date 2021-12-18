from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from main.forms import ContactModelForm
from .models import About, BlogPost, Certification, Contact, Education, Facts, Portfolio

# Create your views here.
def index(request):
    return render(request, 'index.html')


def resume(request):
    educations = Education.objects.all()
    certifications = Certification.objects.all()
    context = {
        'educations':educations,
        'certifications':certifications,
    }
    return render(request, 'resume.html', context=context)

def portfolio(request):
    portfolios = Portfolio.objects.all()
    context = {
        'portfolios':portfolios,
    }
    return render(request, 'portfolio.html', context=context)

def portfolio_single(self, pk):
    portfolios = Portfolio.objects.get(id=pk)
    context = {
        'portfolios':portfolios,
    }
    return render(request, 'portfolio-details.html', context=context)


def service(request):
    return render(request, 'service.html')

def about(request):
    abouts = About.objects.all()
    facts = Facts.objects.all()
    context = {
        'abouts':abouts,
        'facts':facts,
    }
    return render(request, 'about.html', context=context)

def contact(request):
    contacts = Contact.objects.all()
    forms = ContactModelForm()
    if request.method == "POST":
        forms = ContactModelForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
        
    context = {
        'contacts':contacts,
        'forms':forms,
    }
    return render(request, 'contact.html', context=context)

def skills(request):
    return render(request, 'skills.html')

def blog(request):
    posts = BlogPost.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'blog.html', context=context)

def blog_single(request, pk):
    posts = BlogPost.objects.get(id=pk)
    context = {
        'posts':posts,
    }
    return render(request, 'blog-single.html', context=context)