from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.

def scarper(request):
    if request.method == "POST":
        site = request.POST.get('site', "")
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
    # page = requests.get('http://www.facebook.com')
    # soup = BeautifulSoup(page.text, 'html.parser')
    # link_address = []

        for link in soup.find_all('a'):
        # link_address.append(link.get('href'))
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    # return render(request, 'scraper_app/result.html', {'link_address':link_address})
    return render(request, 'scraper_app/result.html', {'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'scraper_app/result.html')