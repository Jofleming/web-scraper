from bs4 import BeautifulSoup
import requests



url = 'https://en.wikipedia.org/wiki/Iliad'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('a', href='/wiki/Wikipedia:Citation_needed')

def get_citations_needed_report():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup('p')

    for result in results:
        body = result.get_text()
        if 'citation needed' in body:
            print(body)

def get_citations_needed_count():
    count = 0
    for anchor in results:
        count += 1
    print(count)

get_citations_needed_count()       
get_citations_needed_report()
