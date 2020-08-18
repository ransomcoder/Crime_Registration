from django.shortcuts import render, redirect
from .models import Bureau, DBTable
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

# Create your views here.
def index(request):
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news=soup_page.findAll("item")
    print(news[0].title.text)

    latest = [news[0], news[1], news[2], news[3], news[4]]

    bureaus = Bureau.objects.all()

    return render(request, "index.html", {'bureaus': bureaus, 'latest': latest})

def new(request):
    if request.method == "POST":
        x = request.POST.get("pname")
        l = x.split('~,')
        print(l)
        DBTable.objects.create(crime_name = l[0], date_reported = l[9], Time_reported = l[10], name_reporter = l[1], address_reporter = l[4], date_crime = l[5], time_crime = l[6], place_offence = l[7], description = l[8], email_reporter = l[3], phone_reporter = l[2])
        p = DBTable.objects.latest('id')
        return render(request, 'submit.html', {'p': p})
    else:
        return render(request, 'new.html')

def services(request):
    return render(request, 'index.html')

def submit(request):
    return render(request, 'submit.html')

