#!
# searchEbay.py opens that first 5 results of a search in Ebay in new tabs

import requests, sys, bs4, webbrowser

# Gets search keywords from the command line arguments.
searchText = ' '.join(sys.argv[1:])

# Ebay's results URL after entering a search
URL = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw='

userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (' \
            'KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

headers = {'User-Agent': userAgent}

print('Searching on Ebay...')  # display text while searching Ebay
# page
page = requests.get(URL + searchText, headers=headers)
page.raise_for_status()

# Retrieve top search results links.
soup = bs4.BeautifulSoup(page.content, features="lxml")

# Open a browser tab for each results
links = soup.find_all('a', {'class': 's-item__link'})

numOpen = min(5, len(links))
for i in range(numOpen):
    webbrowser.open(links[i].get('href'))
