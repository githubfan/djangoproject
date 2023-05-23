# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView): # specifies template for home page
    template_name = "pages/home.html"

class AboutPageView(TemplateView): # specifies template for about page
    template_name = "pages/about.html"

