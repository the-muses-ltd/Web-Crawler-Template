# Basic web crawler designed to mine data from MIT Opencourseware. This can be adapted to be used on any large repository/catalogue of data.
# This tool is intended to make the process of mining data more efficient by automating the process.

import requests
from bs4 import BeautifulSoup

def courses_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'insert website url here'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        # All code from this point on needs to be adapted to the specific structure of the website that the user is attempting to mine data from.
        for link in soup.findAll('h4', {'class': 'course_title'}):
            link_title = link.find('a', {'rel': 'coursePreview'})
            href = 'https://ocw.mit.edu' + link_title.get('href')
            title = link_title.string
            print(title)
            print(href.split('/')[4])
            print(href)
            get_single_course_data(href)
        page += 1

def get_single_course_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_description in soup.findAll('div', {'id': 'description'}):
        description = item_description.findAll('p')
        print(description[0].string)


courses_spider(1)
