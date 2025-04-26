import requests
from bs4 import BeautifulSoup

def scrape_website(url, keywords):
    headers = {'User-Agent': 'SentinelGaruda/1.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    matched = []
    for title in soup.find_all('h2'):
        for keyword in keywords:
            if keyword.lower() in title.text.lower():
                matched.append(title.text.strip())
    return matched
  
