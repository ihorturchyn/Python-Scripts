#!/usr/bin/env python3

import requests, sys, webbrowser, bs4

print('Гуглим...')
pattern_for_search = ('devops metodology')
res = requests.get('https://google.com/search?q=' + pattern_for_search)

## print check if an error has occurred
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElems = soup.select("body a" )

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    print(i)
    webbrowser.open('https://google.com' + linkElems[i].get('href'))
