# amazonParser.py - Given an amazon URL, amazonParser.py will print the
# price of the item. This can be used with scheduling to set an alarm when
# there's a price drop.

import bs4, requests


def getAmazonPrice(productURL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    URL = 'https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=pd_sbs_14_t_0/130-0758958-9551931?_encoding=UTF8&pd_rd_i=1593279922&pd_rd_r=d9e4bee0-68fe-4257-a97f-edd4c2bb5162&pd_rd_w=mJ9yW&pd_rd_wg=ScUjn&pf_rd_p=5cfcfe89-300f-47d2-b1ad-a4e27203a02a&pf_rd_r=JSQGEJ2HR4H16V4Z9JQ8&psc=1&refRID=JSQGEJ2HR4H16V4Z9JQ8'
    res = requests.get(URL, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    elems = soup.select(
        '#buyNewSection > a > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text.strip()


price = getAmazonPrice(
    'https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=pd_sbs_14_t_0/130-0758958-9551931?_encoding=UTF8&pd_rd_i=1593279922&pd_rd_r=d9e4bee0-68fe-4257-a97f-edd4c2bb5162&pd_rd_w=mJ9yW&pd_rd_wg=ScUjn&pf_rd_p=5cfcfe89-300f-47d2-b1ad-a4e27203a02a&pf_rd_r=JSQGEJ2HR4H16V4Z9JQ8&psc=1&refRID=JSQGEJ2HR4H16V4Z9JQ8')
print('The price is ' + price)
