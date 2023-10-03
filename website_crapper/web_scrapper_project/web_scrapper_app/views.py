from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from .models import links


# Create your views here.
def home(request):
    if request.method=='POST':
        a_link=request.POST.get('website','')
        urls=requests.get(a_link)
        beautysoup=BeautifulSoup(urls.text,'html.parser')
        for link in beautysoup.find_all('a'):
            li_add=link.get('href')
            li_name=link.string
            links.objects.create(link_address=li_add, link_name=li_name)
        return redirect('/')
    else:
        val=links.objects.all()
    return render(request,'home.html',{'val':val})