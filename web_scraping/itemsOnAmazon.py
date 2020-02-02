#!
# searchAmazon.py opens that first 5 results of a search in Amazon in new tabs

import requests, sys, bs4, webbrowser

# Gets search keywords from the command line arguments.
searchText = ' '.join(sys.argv[1:])

# Amazon's results URL after entering a search
URL = 'https://www.amazon.com/s?k='

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (' \
            'KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

headers = {'User-Agent': userAgent}

print('Searching on Amazon...')  # display text while searching Amazon
page = requests.get(URL + searchText, headers=headers)
page.raise_for_status()

# Retrieve top search results links.
soup = bs4.BeautifulSoup(page.content, features="lxml")

# Open a browser tab for each results
links = soup.find_all('a', {
    'class': 'a-link-normal a-text-normal'})

numOpen = min(5, len(links))
for i in range(numOpen):
    webbrowser.open('https://www.amazon.com/'+ links[i].get('href'))