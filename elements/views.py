import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def scrape():
    """ returns all divs that have an "zone__item" class on the page """
    html_doc = requests.get('https://www.theonion.com/', headers={'Accept-Encoding':'identity'})
    soup = BeautifulSoup(html_doc.content, "html.parser")

    posts = soup.find_all('div',{'class':'zone__item'})
    print(len(posts))

    for i in posts:
        images = i.find_all('div',{'class':'image-container'})
        print("------------")
        print(images)

scrape()



