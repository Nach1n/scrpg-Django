import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def scrape():
    """ Returns all the titles of the publications in a list. Page: https://www.applesfera.com/"""
    list_titles = []
    html_doc = requests.get('https://www.applesfera.com/', headers={'Accept-Encoding':'identity'})
    soup = BeautifulSoup(html_doc.content, "html.parser")
    publication = soup.find_all('div',{'class':'abstract-content'})
    print(len(publication)) #Return large of de the list publicaction
    
    for i in publication:
        title = i.find('a').getText()
        list_titles.append(title)
        
    for x in list_titles:
        print(x)

scrape()



