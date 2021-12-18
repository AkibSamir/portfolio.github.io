from os import name
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    title1 = models.CharField(max_length=100, blank=True)
    title2 = models.CharField(max_length=100, blank=True)
    sub_title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)
    birthday = models.DateField(auto_now_add=False)
    age = models.IntegerField(null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='profile', blank=True)
    degree = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    city = models.CharField(max_length=200, blank=True)
    freelance = models.CharField(max_length=100, blank=True)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.title1


class Facts(models.Model):
    fact = models.CharField(max_length=100, blank=True)
    clients = models.IntegerField(blank=True, null=True)
    projects = models.IntegerField(blank=True, null=True)
    support = models.IntegerField(blank=True, null=True)
    awards = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.fact

class Education(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    period = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=200, blank=True)
    description = models.TextField( blank=True)

    def __str__(self):
        return self.course_name


class Certification(models.Model):
    course_name = models.CharField(max_length=200, blank=True)
    period = models.CharField(max_length=200, blank=True)
    institute = models.CharField(max_length=200, blank=True)
    description = models.TextField( blank=True)

    def __str__(self):
        return self.course_name


class Contact(models.Model):
    location = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    call = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.location

class ContactForm(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog", default="profile-img.jpg")
    sub_image = models.ImageField(upload_to="blog", blank=True)
    quote = models.CharField(max_length=400, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateField(auto_now_add=True)
    comment = models.IntegerField()
    body = models.TextField()
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title + "|" + str(self.author)


class Portfolio(models.Model):
    title = models.CharField(max_length=200, blank=True)
    category = models.ManyToManyField(Category)
    client = models.CharField(max_length=200, blank=True)
    project_date = models.DateField(auto_now_add=False)
    project_url = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    image1 = models.ImageField(upload_to="portfolio")
    image2 = models.ImageField(upload_to="portfolio")
    image3 = models.ImageField(upload_to="portfolio")
    

    def __str__(self):
        return self.title