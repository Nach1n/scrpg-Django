import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from .models import Page, Imgs

def scrape(request):
    """ Returns all the titles of the publications in a list. Page: https://www.applesfera.com/"""
    template = 'index.html'
    list_titles = []
    list_imgs = []
    html_doc = requests.get('https://www.applesfera.com/', headers={'Accept-Encoding':'identity'})
    soup = BeautifulSoup(html_doc.content, "html.parser")
    publication = soup.find_all('div',{'class':'abstract-content'})
    imgs = soup.find_all('div',{'class':'base-asset-image'})
    
    for i in publication:
        title = i.find('a').getText()
        list_titles.append(title)
    
    for x in imgs:
        images_final = x.find('img').attrs['src']
        list_imgs.append(images_final)

    """ Save elements in BD """
    for i in list_titles:
        Page.objects.create(title=i)

    for j in list_imgs:
        Imgs.objects.create(imgs=j)

    return render(request, template, {})




